"""
LaTeX-based PDF generation tools for cover letters.
Supports English and German with professional formatting.
"""

import os
import re
import subprocess
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from deep_translator import GoogleTranslator
from copy import deepcopy

# Import user configuration
from agent.user_config import config


# ============================================================================
# Pydantic Models
# ============================================================================

class CoverLetterInput(BaseModel):
    """Input schema for cover letter generation"""
    company_name: str = Field(description="Name of the company")
    job_position: str = Field(description="Job position/title being applied for")
    subject: str = Field(description="Subject line for the cover letter")
    intro_paragraph: str = Field(description="Opening paragraph of the cover letter")
    bullet_sections: List[str] = Field(description="List of bullet points highlighting relevant experience")
    closing_paragraph: str = Field(description="Closing paragraph of the cover letter")
    salutation: str = Field(default="Dear Hiring Manager:", description="Salutation line")
    company_address: str = Field(default="", description="Company address if known")


# ============================================================================
# LaTeX Compilation Functions
# ============================================================================

def check_latex_installed() -> Tuple[bool, str]:
    """
    Check if LaTeX is installed on the system.
    
    Returns:
        Tuple of (is_installed: bool, message: str)
    """
    try:
        result = subprocess.run(
            ["pdflatex", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return True, "LaTeX is installed and ready."
        else:
            return False, "pdflatex command failed."
    except FileNotFoundError:
        return False, "LaTeX (pdflatex) is not installed. Please install texlive-full or similar package."
    except Exception as e:
        return False, f"Error checking LaTeX installation: {str(e)}"


def compile_latex_to_pdf(latex_content: str, output_path: str) -> Tuple[bool, str]:
    """
    Compile LaTeX content to PDF.
    
    Args:
        latex_content: LaTeX source code as string
        output_path: Desired output path for the PDF file
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    # Check if LaTeX is installed
    is_installed, msg = check_latex_installed()
    if not is_installed:
        return False, msg
    
    # Create temporary directory for compilation
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Write LaTeX content to temporary .tex file
        tex_file = temp_dir_path / "document.tex"
        tex_file.write_text(latex_content, encoding='utf-8')
        
        try:
            # Compile LaTeX to PDF (run twice for references)
            for _ in range(2):
                result = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "document.tex"],
                    cwd=temp_dir,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            
            # Check if PDF was generated (pdflatex can return non-zero even on success with warnings)
            pdf_file = temp_dir_path / "document.pdf"
            if pdf_file.exists():
                # Ensure output directory exists
                output_dir = Path(output_path).parent
                output_dir.mkdir(parents=True, exist_ok=True)
                
                shutil.copy(pdf_file, output_path)
                return True, f"PDF successfully generated: {output_path}"
            else:
                # PDF was not generated - extract error from log
                log_file = temp_dir_path / "document.log"
                if log_file.exists():
                    log_content = log_file.read_text()
                    # Find the first error line
                    for line in log_content.split('\n'):
                        if line.startswith('!'):
                            return False, f"LaTeX compilation error: {line}"
                return False, "PDF file was not generated."
                
        except subprocess.TimeoutExpired:
            return False, "LaTeX compilation timed out (>30 seconds)."
        except Exception as e:
            return False, f"Error during LaTeX compilation: {str(e)}"


# ============================================================================
# Utility Functions
# ============================================================================

def sanitize_filename(name: str, max_length: int = 30) -> str:
    """Sanitize strings for use in filenames"""
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', name.strip())
    return sanitized[:max_length]


def escape_latex_special_chars(text: str) -> str:
    """
    Escape special LaTeX characters in text to prevent compilation errors.
    Handles: & % $ # _ { } ~ ^ \
    """
    if not text:
        return text
    
    # Order matters - escape backslash first
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    
    result = text
    for char, escaped in replacements:
        result = result.replace(char, escaped)
    
    return result


def translate_to_german(text: str) -> str:
    """Translate text to German using deep_translator"""
    try:
        translator = GoogleTranslator(source='auto', target='de')
        return translator.translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original if translation fails


def get_output_directory(company_name: str, job_position: str) -> Path:
    """
    Generate output directory path following the pattern:
    {BASE_OUTPUT_DIR}/{company_name[:6]}_{job_position[:20]}/
    """
    company_short = sanitize_filename(company_name)[:6]
    position_short = sanitize_filename(job_position)[:20]
    
    dir_name = f"{company_short}_{position_short}"
    output_dir = Path(config.BASE_OUTPUT_DIR) / dir_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return output_dir


def get_date_string(lang: str = "en") -> str:
    """Get formatted date string"""
    now = datetime.now()
    if lang == "de":
        # German date format: 14. Januar 2026
        months_de = ["Januar", "Februar", "März", "April", "Mai", "Juni", 
                     "Juli", "August", "September", "Oktober", "November", "Dezember"]
        return f"{now.day}. {months_de[now.month - 1]} {now.year}"
    else:
        # English date format: January 14, 2026
        return now.strftime("%B %d, %Y")


# ============================================================================
# Cover Letter Generation
# ============================================================================

def load_cover_letter_template(lang: str = "en") -> str:
    """Load cover letter template"""
    template_file = f"cover_letter_{lang}.tex"
    template_path = Path(__file__).parent / "templates" / template_file
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    return template_path.read_text(encoding='utf-8')


def generate_cover_letter_latex(data: CoverLetterInput, lang: str = "en") -> str:
    """
    Generate LaTeX content for cover letter in specified language.
    
    Args:
        data: Cover letter input data
        lang: Language code ('en' or 'de')
        
    Returns:
        LaTeX content as string
    """
    # Load template
    template = load_cover_letter_template(lang)
    
    # Translate content if German
    if lang == "de":
        subject = translate_to_german(data.subject)
        intro_paragraph = translate_to_german(data.intro_paragraph)
        closing_paragraph = translate_to_german(data.closing_paragraph)
        bullet_sections = [translate_to_german(bullet) for bullet in data.bullet_sections]
        salutation = translate_to_german(data.salutation)
        company_name = translate_to_german(data.company_name) if data.company_name else ""
        company_address = translate_to_german(data.company_address) if data.company_address else ""
    else:
        subject = data.subject
        intro_paragraph = data.intro_paragraph
        closing_paragraph = data.closing_paragraph
        bullet_sections = data.bullet_sections
        salutation = data.salutation
        company_name = data.company_name
        company_address = data.company_address
    
    # Escape special LaTeX characters in user-provided content
    subject = escape_latex_special_chars(subject)
    intro_paragraph = escape_latex_special_chars(intro_paragraph)
    closing_paragraph = escape_latex_special_chars(closing_paragraph)
    company_name = escape_latex_special_chars(company_name) if company_name else ""
    company_address = escape_latex_special_chars(company_address) if company_address else ""
    salutation = escape_latex_special_chars(salutation)
    
    # Format bullet points for LaTeX (escape each bullet)
    escaped_bullets = [escape_latex_special_chars(bullet) for bullet in bullet_sections]
    bullet_items = "\n".join([f"  \\item {bullet}" for bullet in escaped_bullets])
    
    # Replace placeholders
    latex_content = template.replace("{{FULL_NAME}}", config.FULL_NAME)
    latex_content = latex_content.replace("{{LOCATION}}", config.LOCATION)
    latex_content = latex_content.replace("{{PHONE}}", config.PHONE)
    latex_content = latex_content.replace("{{EMAIL}}", config.EMAIL)
    latex_content = latex_content.replace("{{LINKEDIN_URL}}", config.LINKEDIN_URL)
    latex_content = latex_content.replace("{{GITHUB_URL}}", config.GITHUB_URL)
    latex_content = latex_content.replace("{{DATE}}", get_date_string(lang))
    latex_content = latex_content.replace("{{COMPANY_NAME}}", company_name)
    latex_content = latex_content.replace("{{COMPANY_ADDRESS}}", company_address)
    latex_content = latex_content.replace("{{SUBJECT}}", subject)
    latex_content = latex_content.replace("{{SALUTATION}}", salutation)
    latex_content = latex_content.replace("{{INTRO_PARAGRAPH}}", intro_paragraph)
    latex_content = latex_content.replace("{{BULLET_SECTIONS}}", bullet_items)
    latex_content = latex_content.replace("{{CLOSING_PARAGRAPH}}", closing_paragraph)
    
    return latex_content


def create_cover_letter_pdf(data: CoverLetterInput, lang: str = "en") -> Tuple[bool, str]:
    """
    Create cover letter PDF in specified language.
    
    Args:
        data: Cover letter input data
        lang: Language code ('en' or 'de')
        
    Returns:
        Tuple of (success: bool, file_path or error_message: str)
    """
    # Get output directory
    output_dir = get_output_directory(data.company_name, data.job_position)
    
    # Generate filename
    lang_suffix = "_de" if lang == "de" else "_en"
    filename = f"{config.NAME_FOR_FILES}_cover_letter{lang_suffix}_{config.CURRENT_YEAR}.pdf"
    output_path = output_dir / filename
    
    # Generate LaTeX content
    latex_content = generate_cover_letter_latex(data, lang)
    
    # Compile to PDF
    success, message = compile_latex_to_pdf(latex_content, str(output_path))
    
    if success:
        return True, str(output_path)
    else:
        return False, message


# ============================================================================
# LangChain Tools
# ============================================================================

@tool("generate-cover-letter-pdfs", args_schema=CoverLetterInput, return_direct=False)
def generate_cover_letter_pdfs(**kwargs) -> str:
    """
    Generate cover letter PDFs in both English and German.
    
    This tool creates professional cover letters in LaTeX format and compiles them to PDF.
    Both English and German versions are generated automatically.
    
    Returns:
        Success message with file paths or error message.
    """
    data = CoverLetterInput(**kwargs)
    
    results = []
    
    # Generate English version
    if config.GENERATE_ENGLISH:
        success_en, path_or_error_en = create_cover_letter_pdf(data, lang="en")
        if success_en:
            results.append(f"✓ English cover letter: {path_or_error_en}")
        else:
            results.append(f"✗ English cover letter failed: {path_or_error_en}")
    
    # Generate German version
    if config.GENERATE_GERMAN:
        success_de, path_or_error_de = create_cover_letter_pdf(data, lang="de")
        if success_de:
            results.append(f"✓ German cover letter: {path_or_error_de}")
        else:
            results.append(f"✗ German cover letter failed: {path_or_error_de}")
    
    return "\n".join(results)


@tool("edit-cover-letter-pdfs", args_schema=CoverLetterInput, return_direct=False)
def edit_cover_letter_pdfs(**kwargs) -> str:
    """
    Edit and regenerate cover letter PDFs in both English and German.
    
    This tool regenerates the cover letters with updated content.
    
    Returns:
        Success message with file paths or error message.
    """
    # Reuse the generate function since we're overwriting anyway
    return generate_cover_letter_pdfs(**kwargs)
