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
# Resume Tailoring Models
# ============================================================================

class ResumeBulletPoint(BaseModel):
    """Single bullet point from resume"""
    original_text: str = Field(description="Original bullet point text from resume")
    tailored_text: str = Field(description="ATS-optimized version with job keywords")


class ResumeExperienceSection(BaseModel):
    """Professional experience entry"""
    job_title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    bullet_points: List[ResumeBulletPoint] = Field(description="List of bullet points for this role")


class ResumeProjectSection(BaseModel):
    """Project entry"""
    project_name: str = Field(description="Project name")
    bullet_points: List[ResumeBulletPoint] = Field(description="List of bullet points for this project")


class ResumeHackathonSection(BaseModel):
    """Hackathon project entry"""
    project_name: str = Field(description="Hackathon project name")
    description: ResumeBulletPoint = Field(description="Single description paragraph")


class ResumeInput(BaseModel):
    """Input schema for resume tailoring"""
    company_name: str = Field(description="Target company name")
    job_position: str = Field(description="Job position/title being applied for")
    job_description: str = Field(description="Full job description text to optimize resume for")


class TailoredResumeOutput(BaseModel):
    """Output schema containing all tailored resume sections"""
    experience_sections: List[ResumeExperienceSection] = Field(description="Tailored professional experience")
    project_sections: List[ResumeProjectSection] = Field(description="Tailored projects")
    hackathon_sections: List[ResumeHackathonSection] = Field(description="Tailored hackathon projects")
    skills: str = Field(description="Updated skills line with relevant skills for this job")


# ============================================================================
# Resume Template Functions
# ============================================================================

def load_resume_template() -> str:
    """Load the resume LaTeX template"""
    template_path = Path(__file__).parent / "templates" / "resume_en.tex"
    if not template_path.exists():
        raise FileNotFoundError(f"Resume template not found: {template_path}")
    return template_path.read_text(encoding='utf-8')


def parse_resume_sections(latex_content: str) -> Dict[str, any]:
    """
    Parse LaTeX resume into structured sections.
    
    Returns:
        Dict containing:
        - experience: List of dicts with job_title, company, bullets
        - projects: List of dicts with project_name, bullets
        - hackathons: List of dicts with project_name, description
        - skills: str with skills line
    """
    result = {
        "experience": [],
        "projects": [],
        "hackathons": [],
        "skills": ""
    }
    
    # Extract Professional Work Experience section
    exp_match = re.search(
        r'\\begin{rSection}{Professional Work Experience}(.*?)\\end{rSection}',
        latex_content, re.DOTALL
    )
    if exp_match:
        exp_content = exp_match.group(1)
        # Find each job entry
        job_pattern = r'\\textbf{([^}]+)}.*?\\href{[^}]+}{([^}]+)}.*?\\begin{itemize}(.*?)\\end{itemize}'
        for job_match in re.finditer(job_pattern, exp_content, re.DOTALL):
            bullets = re.findall(r'\\item\s+(.*?)(?=\\item|$)', job_match.group(3), re.DOTALL)
            bullets = [b.strip() for b in bullets if b.strip()]
            result["experience"].append({
                "job_title": job_match.group(1).replace("\\&", "&"),
                "company": job_match.group(2),
                "bullets": bullets
            })
    
    # Extract Projects section
    proj_match = re.search(
        r'\\begin{rSection}{Projects}(.*?)\\end{rSection}',
        latex_content, re.DOTALL
    )
    if proj_match:
        proj_content = proj_match.group(1)
        # Find each project entry
        project_pattern = r'\\item\s+\\textbf{([^}]+)}.*?\\begin{itemize}(.*?)\\end{itemize}'
        for proj in re.finditer(project_pattern, proj_content, re.DOTALL):
            bullets = re.findall(r'\\item\s+(.*?)(?=\\item|$)', proj.group(2), re.DOTALL)
            bullets = [b.strip() for b in bullets if b.strip()]
            result["projects"].append({
                "project_name": proj.group(1),
                "bullets": bullets
            })
    
    # Extract Hackathon Projects section
    hack_match = re.search(
        r'\\begin{rSection}{Hackathon Projects}(.*?)\\end{rSection}',
        latex_content, re.DOTALL
    )
    if hack_match:
        hack_content = hack_match.group(1)
        # Extract each item in the hackathon section
        hack_items = re.findall(r'\\item\s+(.*?)(?=\\item|$)', hack_content, re.DOTALL)
        for item in hack_items:
            # Extract project name from \textbf{\href{...}{NAME}} or \textbf{NAME}
            name_match = re.search(r'\\textbf{(?:\\href{[^}]+})?{?([^}]+)}?}', item)
            if name_match:
                project_name = name_match.group(1)
                # Get description - everything after the first line
                lines = item.strip().split('\n')
                if len(lines) > 1:
                    desc = ' '.join(lines[1:]).strip()
                    desc = re.sub(r'\s+', ' ', desc)
                else:
                    desc = ""
                result["hackathons"].append({
                    "project_name": project_name,
                    "description": desc
                })
    
    # Extract Skills section
    skills_match = re.search(
        r'\\begin{rSection}{Skills}\s*(.*?)\s*\\end{rSection}',
        latex_content, re.DOTALL
    )
    if skills_match:
        result["skills"] = skills_match.group(1).strip()
    
    return result


def validate_bullet_preservation(original: str, tailored: str, section_name: str) -> Tuple[bool, str]:
    """
    Validate that tailored bullet preserves critical elements from original.

    Focus on preserving:
    - Numbers, metrics, percentages (MUST be preserved)
    - Company names (MUST be preserved)
    - Core technologies (MUST be preserved)

    Also validates surgical edit constraint (<25% change).

    Args:
        original: Original bullet text
        tailored: Tailored bullet text
        section_name: Name of section for error reporting

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Extract all numbers (including percentages, decimals, and counts)
    # These MUST be preserved - no changes allowed
    number_pattern = r'\d+(?:[.,]\d+)?%?(?:\+)?'
    original_numbers = set(re.findall(number_pattern, original))
    tailored_numbers = set(re.findall(number_pattern, tailored))

    missing_numbers = original_numbers - tailored_numbers
    if missing_numbers:
        return False, f"{section_name}: Missing numbers/metrics: {missing_numbers}"

    # Check for company/institution names (these MUST be preserved)
    company_keywords = ['Brandl', 'Nutrition', 'Braunschweig', 'SciBiome', 'TECHR', 'TU']
    for keyword in company_keywords:
        if keyword in original and keyword not in tailored:
            return False, f"{section_name}: Missing company/institution name: {keyword}"

    # Validate surgical edit constraint - changes should be minimal
    # Calculate word-level difference
    original_words = set(original.lower().split())
    tailored_words = set(tailored.lower().split())

    # Words that were removed (should be very few)
    removed_words = original_words - tailored_words
    # Filter out common words that might be rephrased
    significant_removed = {w for w in removed_words if len(w) > 3}

    # If more than 25% of original words were removed, flag it
    if len(original_words) > 0:
        removal_ratio = len(significant_removed) / len(original_words)
        if removal_ratio > 0.25:
            return False, f"{section_name}: Too many words removed ({len(significant_removed)} words, {removal_ratio:.0%}). Surgical edits should preserve >75% of original text."

    return True, ""


def calculate_edit_percentage(original: str, tailored: str) -> float:
    """
    Calculate the percentage of text that was changed.

    Returns:
        Float between 0 and 1 representing change percentage.
    """
    original_words = original.lower().split()
    tailored_words = tailored.lower().split()

    if not original_words:
        return 1.0

    # Count words that appear in both
    original_set = set(original_words)
    tailored_set = set(tailored_words)

    preserved = len(original_set & tailored_set)
    total_original = len(original_set)

    preservation_ratio = preserved / total_original if total_original > 0 else 0
    return 1.0 - preservation_ratio


def extract_jd_keywords(job_description: str) -> Dict[str, List[str]]:
    """
    Extract technical keywords from a job description.

    Returns:
        Dict with categories: languages, frameworks, tools, cloud, databases, concepts
    """
    jd_lower = job_description.lower()

    # Define keyword patterns
    keyword_categories = {
        "languages": [
            "python", "java", "javascript", "typescript", "c++", "c#", "go", "golang",
            "rust", "scala", "kotlin", "ruby", "php", "swift", "r", "matlab", "sql", "bash"
        ],
        "frameworks": [
            "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn", "fastapi", "flask",
            "django", "react", "nextjs", "next.js", "vue", "angular", "express", "spring",
            "langchain", "langgraph", "langsmith", "huggingface", "transformers"
        ],
        "libraries": [
            "numpy", "pandas", "opencv", "pillow", "pil", "matplotlib", "seaborn",
            "scipy", "nltk", "spacy", "beautifulsoup", "selenium", "playwright"
        ],
        "cloud_devops": [
            "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "k8s",
            "ci/cd", "jenkins", "github actions", "terraform", "ansible", "mlflow",
            "mlops", "airflow", "prefect", "dagster"
        ],
        "databases": [
            "postgresql", "postgres", "mysql", "mongodb", "redis", "elasticsearch",
            "qdrant", "pinecone", "weaviate", "neo4j", "dynamodb", "bigquery"
        ],
        "ai_ml_concepts": [
            "machine learning", "deep learning", "nlp", "natural language processing",
            "computer vision", "llm", "large language model", "rag", "retrieval augmented",
            "vector database", "embeddings", "fine-tuning", "prompt engineering",
            "reinforcement learning", "time series", "forecasting", "recommendation"
        ],
        "soft_concepts": [
            "production", "scalable", "distributed", "real-time", "batch processing",
            "data pipeline", "etl", "api", "rest api", "graphql", "microservices",
            "agile", "cross-functional", "full-stack", "end-to-end"
        ]
    }

    found_keywords = {cat: [] for cat in keyword_categories}

    for category, keywords in keyword_categories.items():
        for keyword in keywords:
            if keyword in jd_lower:
                # Capitalize properly for display
                display_keyword = keyword.title() if len(keyword) > 3 else keyword.upper()
                if keyword == "ci/cd":
                    display_keyword = "CI/CD"
                elif keyword == "llm":
                    display_keyword = "LLMs"
                elif keyword == "nlp":
                    display_keyword = "NLP"
                elif keyword == "rag":
                    display_keyword = "RAG"
                elif keyword == "api":
                    display_keyword = "API"
                elif keyword == "rest api":
                    display_keyword = "REST APIs"
                found_keywords[category].append(display_keyword)

    return found_keywords


def map_keywords_to_projects(keywords: Dict[str, List[str]], sections: Dict) -> Dict[str, List[str]]:
    """
    Map extracted keywords to relevant resume sections based on project content.

    CONSERVATIVE APPROACH: Only suggest keywords that are DEFINITELY TRUE.
    - Only implicit/standard dependencies (NumPy with PyTorch)
    - Only more specific names for existing tech (Qdrant → "vector database")
    - NEVER suggest tech that wasn't actually used

    Returns:
        Dict mapping project/experience names to relevant keywords that can be added.
    """
    keyword_mapping = {}

    # Flatten all keywords
    all_keywords = []
    for cat_keywords in keywords.values():
        all_keywords.extend(cat_keywords)

    # CONSERVATIVE keyword mappings - ONLY suggest what's definitely true
    # Format: "hint in text" → [keywords that are IMPLICIT/DEFINITELY USED]
    project_tech_hints = {
        # Experience sections - CONSERVATIVE
        "Prophet-based": ["Python", "Pandas"],  # Prophet uses Python/Pandas
        "AWS pipeline": ["Docker"],  # ECS uses Docker containers
        "AWS": ["Docker"],  # AWS ECS = Docker
        "ECS": ["Docker"],  # ECS runs Docker
        "Email Agent": ["LLMs"],  # AI agent uses LLMs
        "n8n": ["API"],  # n8n integrations use APIs
        "Google Gemini": ["LLMs"],  # Gemini IS an LLM
        "FastAPI": ["API", "REST APIs"],  # FastAPI creates APIs
        "LangGraph": ["LLMs"],  # LangGraph orchestrates LLMs
        "Qdrant": ["Vector Database"],  # Qdrant IS a vector DB
        "CycleGAN": ["Deep Learning", "Computer Vision"],  # CycleGAN is DL + CV
        "TensorFlow": ["Deep Learning"],  # TensorFlow is DL framework
        "PyTorch": ["NumPy"],  # PyTorch depends on NumPy
        "OpenCV": ["Computer Vision"],  # OpenCV IS computer vision
        "Real-ESRGAN": ["Computer Vision", "Deep Learning"],  # ESRGAN is DL + CV
        "KBNet": ["Deep Learning"],  # KBNet is DL model

        # Projects - CONSERVATIVE
        "LLM-powered": ["LLMs", "NLP"],  # LLM-powered = uses LLMs
        "discourse analysis": ["NLP"],  # Discourse analysis IS NLP
        "tweets": ["NLP"],  # Tweet analysis = NLP
        "multi-agent": ["LLMs"],  # Multi-agent systems use LLMs
        "Gemini": ["LLMs"],  # Gemini IS an LLM
        "DeepSeek": ["LLMs"],  # DeepSeek IS an LLM
        "pose estimation": ["Computer Vision"],  # Pose estimation IS CV

        # Hackathons - CONSERVATIVE
        "YOLOv": ["Computer Vision", "Deep Learning"],  # YOLO is CV + DL
        "research agent": ["LLMs"],  # Research agents use LLMs

        # NOTE: We do NOT auto-suggest these (require explicit proof):
        # - "RAG" (only if there's actual retrieval)
        # - "CI/CD" (only if automated deployment)
        # - "MLOps" (only if ML lifecycle management)
        # - "Kubernetes" (only if K8s is used, not just Docker)
    }

    # Map keywords to each section
    for exp in sections.get("experience", []):
        relevant = []
        exp_str = str(exp).lower()
        for hint, tech_list in project_tech_hints.items():
            if hint.lower() in exp_str:
                for tech in tech_list:
                    if tech in all_keywords and tech not in relevant:
                        relevant.append(tech)
        if relevant:
            keyword_mapping[f"{exp.get('job_title', '')} at {exp.get('company', '')}"] = relevant

    for proj in sections.get("projects", []):
        relevant = []
        proj_str = str(proj).lower()
        for hint, tech_list in project_tech_hints.items():
            if hint.lower() in proj_str:
                for tech in tech_list:
                    if tech in all_keywords and tech not in relevant:
                        relevant.append(tech)
        if relevant:
            keyword_mapping[proj.get("project_name", "")] = relevant

    for hack in sections.get("hackathons", []):
        relevant = []
        hack_str = str(hack).lower()
        for hint, tech_list in project_tech_hints.items():
            if hint.lower() in hack_str:
                for tech in tech_list:
                    if tech in all_keywords and tech not in relevant:
                        relevant.append(tech)
        if relevant:
            keyword_mapping[hack.get("project_name", "")] = relevant

    return keyword_mapping



def replace_text_robust(latex_content: str, original: str, replacement: str) -> str:
    """
    Replace text robustly by matching words regardless of whitespace.
    Handles LaTeX special characters and whitespace normalization.
    """
    if not original or not original.strip():
        return latex_content

    # Strategy 1: Direct replacement (exact match)
    if original in latex_content:
        return latex_content.replace(original, replacement, 1)

    # Strategy 2: Word-based pattern matching (handles whitespace/newlines)
    words = original.split()
    if not words:
        return latex_content

    # Create pattern: escape words, join with flexible whitespace
    pattern = r'\s+'.join(re.escape(w) for w in words)
    new_content = re.sub(pattern, lambda m: replacement, latex_content, count=1)
    if new_content != latex_content:
        return new_content

    # Strategy 3: Handle LaTeX escape differences
    # The agent might send "80%" but LaTeX has "80\%"
    # Create a pattern that matches both escaped and unescaped versions
    def make_latex_flexible(word: str) -> str:
        """Make a word pattern that matches LaTeX escapes flexibly."""
        # Handle percentage
        word = re.sub(r'(\d+)%', r'\1\\\\?%', word)
        # Handle ampersand
        word = word.replace('&', r'\\?&')
        # Handle other special chars that might be escaped
        return word

    flexible_words = [make_latex_flexible(re.escape(w)) for w in words]
    flex_pattern = r'\s+'.join(flexible_words)

    try:
        new_content = re.sub(flex_pattern, lambda m: replacement, latex_content, count=1)
        if new_content != latex_content:
            return new_content
    except re.error:
        pass  # If pattern is invalid, continue to next strategy

    # Strategy 4: Find longest matching substring and replace around it
    # This handles cases where original text is slightly different
    # Find a unique anchor (like a specific metric or tech name)
    for anchor in re.findall(r'\d+[%+]?|\b[A-Z][a-z]+[A-Z]\w*\b|\b(?:Prophet|Chronos|Moirai|LangGraph|FastAPI)\b', original):
        # Find this anchor in the LaTeX content
        anchor_escaped = re.escape(anchor).replace(r'\%', r'\\?%')
        anchor_matches = list(re.finditer(anchor_escaped, latex_content))

        for match in anchor_matches:
            # Get context around the anchor (the full bullet)
            start = match.start()
            end = match.end()

            # Expand to find the full item (between \item and next \item or \end)
            line_start = latex_content.rfind('\\item', 0, start)
            if line_start == -1:
                continue
            line_end = latex_content.find('\\item', end)
            if line_end == -1:
                line_end = latex_content.find('\\end{itemize}', end)
            if line_end == -1:
                line_end = len(latex_content)

            bullet_text = latex_content[line_start:line_end]

            # Check if this bullet contains most of our original words
            original_word_set = set(w.lower() for w in words if len(w) > 3)
            bullet_word_set = set(w.lower() for w in bullet_text.split() if len(w) > 3)

            overlap = len(original_word_set & bullet_word_set) / len(original_word_set) if original_word_set else 0

            if overlap > 0.7:  # 70% word overlap means it's likely the right bullet
                # Replace the content after \item
                item_content_start = line_start + len('\\item')
                # Skip whitespace
                while item_content_start < line_end and latex_content[item_content_start] in ' \t\n':
                    item_content_start += 1

                old_bullet_content = latex_content[item_content_start:line_end].strip()
                new_content = latex_content[:item_content_start] + ' ' + replacement + latex_content[line_end:]
                return new_content

    # If all strategies fail, return unchanged
    print(f"⚠️ WARNING: Could not find text to replace: {original[:50]}...")
    return latex_content


def generate_tailored_resume_latex(
    original_latex: str,
    tailored_output: TailoredResumeOutput
) -> str:
    """
    Generate tailored resume LaTeX by replacing bullet points with tailored versions.

    Validates that:
    1. Critical elements are preserved (numbers, companies, technologies)
    2. Surgical edit constraint is met (<25% text change)

    Raises ValueError if validation fails.
    """
    latex = original_latex
    validation_errors = []
    edit_stats = []

    # Replace and validate experience bullets
    for exp in tailored_output.experience_sections:
        section_name = f"{exp.job_title} at {exp.company}"
        for i, bp in enumerate(exp.bullet_points):
            if bp.original_text and bp.tailored_text:
                # Validate preservation
                is_valid, error_msg = validate_bullet_preservation(
                    bp.original_text,
                    bp.tailored_text,
                    f"{section_name} (bullet {i+1})"
                )
                if not is_valid:
                    validation_errors.append(error_msg)
                else:
                    # Track edit percentage
                    edit_pct = calculate_edit_percentage(bp.original_text, bp.tailored_text)
                    edit_stats.append((f"{section_name} bullet {i+1}", edit_pct))

                    # Escape LaTeX special characters in tailored text
                    escaped_tailored = escape_latex_special_chars(bp.tailored_text)
                    # Robust replacement handling whitespace
                    latex = replace_text_robust(latex, bp.original_text, escaped_tailored)

    # Replace and validate project bullets
    for proj in tailored_output.project_sections:
        section_name = f"Project: {proj.project_name}"
        for i, bp in enumerate(proj.bullet_points):
            if bp.original_text and bp.tailored_text:
                # Validate preservation
                is_valid, error_msg = validate_bullet_preservation(
                    bp.original_text,
                    bp.tailored_text,
                    f"{section_name} (bullet {i+1})"
                )
                if not is_valid:
                    validation_errors.append(error_msg)
                else:
                    # Track edit percentage
                    edit_pct = calculate_edit_percentage(bp.original_text, bp.tailored_text)
                    edit_stats.append((f"{section_name} bullet {i+1}", edit_pct))

                    # Escape LaTeX special characters in tailored text
                    escaped_tailored = escape_latex_special_chars(bp.tailored_text)
                    # Robust replacement handling whitespace
                    latex = replace_text_robust(latex, bp.original_text, escaped_tailored)

    # Replace and validate hackathon descriptions
    for hack in tailored_output.hackathon_sections:
        if hack.description.original_text and hack.description.tailored_text:
            section_name = f"Hackathon: {hack.project_name}"
            is_valid, error_msg = validate_bullet_preservation(
                hack.description.original_text,
                hack.description.tailored_text,
                section_name
            )
            if not is_valid:
                validation_errors.append(error_msg)
            else:
                # Track edit percentage
                edit_pct = calculate_edit_percentage(hack.description.original_text, hack.description.tailored_text)
                edit_stats.append((section_name, edit_pct))

                # Escape LaTeX special characters in tailored text
                escaped_tailored = escape_latex_special_chars(hack.description.tailored_text)
                latex = replace_text_robust(latex, hack.description.original_text, escaped_tailored)

    # Check for excessive edits (non-surgical)
    excessive_edits = [(name, pct) for name, pct in edit_stats if pct > 0.30]
    if excessive_edits:
        for name, pct in excessive_edits:
            validation_errors.append(
                f"⚠️ {name}: {pct:.0%} of words changed. Surgical edits should change <25% of text."
            )

    # If there are validation errors, raise exception with details
    if validation_errors:
        error_summary = "\n".join(validation_errors)
        raise ValueError(
            f"Resume tailoring validation FAILED:\n\n{error_summary}\n\n"
            f"SURGICAL EDIT RULES:\n"
            f"1. Preserve ALL numbers, metrics, and company names\n"
            f"2. Change <25% of original text (only APPEND keywords)\n"
            f"3. DO NOT rewrite entire bullets\n\n"
            f"Example of correct surgical edit:\n"
            f"BEFORE: 'Built pipeline using PyTorch'\n"
            f"AFTER:  'Built pipeline using PyTorch, OpenCV, and NumPy'\n"
            f"(Only appended ', OpenCV, and NumPy')"
        )

    # Log edit statistics for transparency
    if edit_stats:
        avg_edit = sum(pct for _, pct in edit_stats) / len(edit_stats)
        print(f"📊 Surgical Edit Stats: Average {avg_edit:.0%} text changed across {len(edit_stats)} bullets")

    # Replace skills section
    if tailored_output.skills:
        # Escape LaTeX special characters in skills text
        escaped_skills = escape_latex_special_chars(tailored_output.skills)
        skills_pattern = r'(\\begin{rSection}{Skills}\s*).*?(\s*\\end{rSection})'
        latex = re.sub(
            skills_pattern,
            rf'\1{escaped_skills}\2',
            latex,
            flags=re.DOTALL
        )

    return latex


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
        
        # Copy resume.cls if the document uses it
        if r'\documentclass' in latex_content and 'resume' in latex_content[:500]:
            resume_cls_path = Path(__file__).parent / "templates" / "resume.cls"
            if resume_cls_path.exists():
                shutil.copy(resume_cls_path, temp_dir_path / "resume.cls")
        
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


# ============================================================================
# Resume Tailoring Functions
# ============================================================================

def create_tailored_resume_pdf(
    tailored_output: TailoredResumeOutput,
    company_name: str,
    job_position: str
) -> Tuple[bool, str]:
    """
    Create tailored resume PDF.
    
    Args:
        tailored_output: Structured output with tailored sections
        company_name: Target company name
        job_position: Job position for filename
        
    Returns:
        Tuple of (success: bool, file_path or error_message: str)
    """
    # Load original template
    original_latex = load_resume_template()
    
    # Generate tailored LaTeX
    tailored_latex = generate_tailored_resume_latex(original_latex, tailored_output)
    
    # Get output directory
    output_dir = get_output_directory(company_name, job_position)
    
    # Generate filename
    filename = f"{config.NAME_FOR_FILES}_resume_{config.CURRENT_YEAR}.pdf"
    output_path = output_dir / filename
    
    # Also save the .tex file for reference
    tex_filename = f"{config.NAME_FOR_FILES}_resume_{config.CURRENT_YEAR}.tex"
    tex_path = output_dir / tex_filename
    tex_path.write_text(tailored_latex, encoding='utf-8')
    
    # Compile to PDF
    success, message = compile_latex_to_pdf(tailored_latex, str(output_path))
    
    if success:
        return True, str(output_path)
    else:
        return False, message


@tool("tailor-resume-for-ats", args_schema=ResumeInput, return_direct=False)
def tailor_resume_for_ats(**kwargs) -> str:
    """
    Tailor resume for a specific job description to optimize ATS score.

    This tool analyzes the job description, extracts keywords, and returns
    the current resume content with SURGICAL EDIT instructions.

    SURGICAL EDITS = Keep 75%+ of original text, only ADD relevant keywords.

    After editing, use the generate-tailored-resume-pdf tool to create the PDF.

    Returns:
        Current resume sections with keyword mapping for surgical edits.
    """
    data = ResumeInput(**kwargs)

    # Load and parse current resume
    try:
        latex_content = load_resume_template()
        sections = parse_resume_sections(latex_content)
    except Exception as e:
        return f"Error loading resume template: {str(e)}"

    # Extract keywords from JD
    jd_keywords = extract_jd_keywords(data.job_description)

    # Map keywords to projects
    keyword_mapping = map_keywords_to_projects(jd_keywords, sections)

    # Format output for the agent
    output_parts = []
    output_parts.append("=" * 70)
    output_parts.append("RESUME TAILORING TASK - SURGICAL KEYWORD INJECTION")
    output_parts.append("=" * 70)
    output_parts.append(f"\nTarget Company: {data.company_name}")
    output_parts.append(f"Target Position: {data.job_position}")

    # Show extracted keywords
    output_parts.append(f"\n{'=' * 70}")
    output_parts.append("EXTRACTED JD KEYWORDS (Add these to Skills + relevant bullets)")
    output_parts.append("=" * 70)

    for category, keywords in jd_keywords.items():
        if keywords:
            output_parts.append(f"\n{category.upper()}: {', '.join(keywords)}")

    # Flatten for skills section
    all_keywords = []
    for kw_list in jd_keywords.values():
        all_keywords.extend(kw_list)
    output_parts.append(f"\n\n🎯 ALL JD KEYWORDS FOR SKILLS SECTION:\n{', '.join(all_keywords)}")

    # Show keyword-to-project mapping
    output_parts.append(f"\n{'=' * 70}")
    output_parts.append("KEYWORD-TO-PROJECT MAPPING (Which keywords to add where)")
    output_parts.append("=" * 70)

    if keyword_mapping:
        for project, keywords in keyword_mapping.items():
            output_parts.append(f"\n📌 {project}")
            output_parts.append(f"   Add: {', '.join(keywords)}")
    else:
        output_parts.append("\nNo automatic mapping found. Use judgment to add relevant keywords.")

    output_parts.append(f"\n{'=' * 70}")
    output_parts.append("JOB DESCRIPTION (Reference)")
    output_parts.append("=" * 70)
    output_parts.append(data.job_description[:2000] + "..." if len(data.job_description) > 2000 else data.job_description)

    output_parts.append(f"\n{'=' * 70}")
    output_parts.append("CURRENT RESUME SECTIONS - MAKE SURGICAL EDITS ONLY")
    output_parts.append("=" * 70)

    # Professional Experience with surgical edit hints
    output_parts.append("\n" + "-" * 50)
    output_parts.append("PROFESSIONAL EXPERIENCE")
    output_parts.append("-" * 50)
    for i, exp in enumerate(sections["experience"], 1):
        section_key = f"{exp['job_title']} at {exp['company']}"
        suggested_keywords = keyword_mapping.get(section_key, [])

        output_parts.append(f"\n[Experience {i}] {exp['job_title']} at {exp['company']}")
        if suggested_keywords:
            output_parts.append(f"   💡 Suggested keywords to ADD: {', '.join(suggested_keywords)}")

        for j, bullet in enumerate(exp["bullets"], 1):
            output_parts.append(f"\n  ORIGINAL Bullet {j}:")
            output_parts.append(f"  {bullet}")
            output_parts.append(f"  ↳ SURGICAL EDIT: Append 3-6 relevant keywords (e.g., ', using X, Y, and Z'); do not remove details")

    # Projects
    output_parts.append("\n" + "-" * 50)
    output_parts.append("PROJECTS")
    output_parts.append("-" * 50)
    for i, proj in enumerate(sections["projects"], 1):
        section_key = proj['project_name']
        suggested_keywords = keyword_mapping.get(section_key, [])

        output_parts.append(f"\n[Project {i}] {proj['project_name']}")
        if suggested_keywords:
            output_parts.append(f"   💡 Suggested keywords to ADD: {', '.join(suggested_keywords)}")

        for j, bullet in enumerate(proj["bullets"], 1):
            output_parts.append(f"\n  ORIGINAL Bullet {j}:")
            output_parts.append(f"  {bullet}")
            output_parts.append(f"  ↳ SURGICAL EDIT: Append 3-6 relevant keywords; do not remove details")

    # Hackathons
    output_parts.append("\n" + "-" * 50)
    output_parts.append("HACKATHON PROJECTS")
    output_parts.append("-" * 50)
    for i, hack in enumerate(sections["hackathons"], 1):
        section_key = hack['project_name']
        suggested_keywords = keyword_mapping.get(section_key, [])

        output_parts.append(f"\n[Hackathon {i}] {hack['project_name']}")
        if suggested_keywords:
            output_parts.append(f"   💡 Suggested keywords to ADD: {', '.join(suggested_keywords)}")
        output_parts.append(f"\n  ORIGINAL Description:")
        output_parts.append(f"  {hack['description']}")
        output_parts.append(f"  ↳ SURGICAL EDIT: Append 3-6 relevant keywords; do not remove details")

    # Skills
    output_parts.append("\n" + "-" * 50)
    output_parts.append("SKILLS SECTION (REWRITE COMPLETELY)")
    output_parts.append("-" * 50)
    output_parts.append(f"\nCURRENT: {sections['skills']}")
    output_parts.append(f"\n🎯 NEW SKILLS should include ALL these JD keywords FIRST:")
    output_parts.append(f"{', '.join(all_keywords)}")
    output_parts.append("\nThen add relevant existing skills.")

    output_parts.append(f"\n{'=' * 70}")
    output_parts.append("⚠️ SURGICAL EDIT RULES - FOLLOW EXACTLY")
    output_parts.append("=" * 70)
    output_parts.append("""
1. SKILLS SECTION: Rewrite completely with ALL JD keywords first

2. BULLET POINTS: SURGICAL EDITS ONLY
   ✅ DO: Add keywords at the end: "original text, using X, Y, and Z"
   ✅ DO: Expand tech lists: "(X, Y)" → "(X, Y, Z)"
   ❌ DON'T: Rewrite entire bullet structure
   ❌ DON'T: Remove any original technologies
   ❌ DON'T: Change any numbers/metrics

3. PRESERVATION RULE: 75%+ of original text must remain unchanged (no detail loss)

4. BANNED PHRASES (Never use):
   - "deployment optimization"
   - "methodologies"
   - "demonstrated familiarity with"
   - "showcasing abilities in"

⚠️ TRUTHFULNESS IS NON-NEGOTIABLE:
   ❌ NEVER add "RAG" unless there's actual retrieval from a knowledge base
   ❌ NEVER add "LLMs" to projects that don't use language models
   ❌ NEVER add "CI/CD" unless there's automated deployment
   ❌ NEVER add technologies you didn't actually use

   ✅ SAFE TO ADD (implicit dependencies):
   - PyTorch → "NumPy" (standard dependency)
   - OpenCV → "Computer Vision" (that's what it is)
   - Qdrant → "vector database" (Qdrant IS a vector DB)
   - LangGraph/Gemini → "LLMs" (they use LLMs)
   - FastAPI → "REST APIs" (FastAPI creates REST APIs)

EXAMPLE SURGICAL EDIT:
BEFORE: "Built pipeline using PyTorch for image enhancement"
AFTER:  "Built pipeline using PyTorch, OpenCV, and NumPy for image enhancement"
(Only added ", OpenCV, and NumPy" - rest is identical)

Now call generate-tailored-resume-pdf with surgically edited bullets.
""")

    return "\n".join(output_parts)


class TailoredResumeInput(BaseModel):
    """Input for generating tailored resume PDF"""
    company_name: str = Field(description="Target company name")
    job_position: str = Field(description="Job position being applied for")
    experience_sections: List[ResumeExperienceSection] = Field(
        description="Tailored professional experience sections"
    )
    project_sections: List[ResumeProjectSection] = Field(
        description="Tailored project sections"
    )
    hackathon_sections: List[ResumeHackathonSection] = Field(
        description="Tailored hackathon project sections"
    )
    skills: str = Field(description="Updated skills line")


@tool("generate-tailored-resume-pdf", args_schema=TailoredResumeInput, return_direct=False)
def generate_tailored_resume_pdf(**kwargs) -> str:
    """
    Generate a tailored resume PDF with ATS-optimized content.
    
    This tool takes the rewritten resume sections and generates a PDF.
    Use this after tailor-resume-for-ats and rewriting the content.
    
    Returns:
        Success message with file path or error message.
    """
    data = TailoredResumeInput(**kwargs)
    
    # Convert to TailoredResumeOutput
    tailored_output = TailoredResumeOutput(
        experience_sections=data.experience_sections,
        project_sections=data.project_sections,
        hackathon_sections=data.hackathon_sections,
        skills=data.skills
    )
    
    # Generate PDF
    success, path_or_error = create_tailored_resume_pdf(
        tailored_output,
        data.company_name,
        data.job_position
    )
    
    if success:
        return f"✓ Tailored resume generated: {path_or_error}"
    else:
        return f"✗ Resume generation failed: {path_or_error}"
