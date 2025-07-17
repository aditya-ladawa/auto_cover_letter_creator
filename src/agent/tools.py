from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import mm
import os
import re
from datetime import datetime
from langchain_core.tools import tool
from pydantic import BaseModel

from deep_translator import GoogleTranslator
from copy import deepcopy



class CoverLetterInput(BaseModel):
    company_name: str
    job_post: str
    address: str | None = None
    subject: str
    intro_paragraph: str
    bullet_sections: list[str]
    closing_paragraph: str
    sign_off: str = "Regards,"
    sender_name: str = "Aditya Ghanashyam Ladawa"
    location: str = "Braunschweig, Germany"
    phone: str = "+49 15510 030840"
    email: str = "adityaladawa12@gmail.com"
    github_url: str = "https://github.com/aditya-ladawa"
    linkedin_url: str = "https://www.linkedin.com/in/aditya-ladawa/"


def translate_cover_letter_input_to_german(data: CoverLetterInput) -> CoverLetterInput:
    translator = GoogleTranslator(source='auto', target='de')
    
    # Create a deep copy to avoid mutating original
    german_data = deepcopy(data)

    # Translate scalar text fields
    german_data.subject = translator.translate(data.subject)
    german_data.intro_paragraph = translator.translate(data.intro_paragraph)
    german_data.closing_paragraph = translator.translate(data.closing_paragraph)
    german_data.company_name = translator.translate(data.company_name) if data.company_name else None
    german_data.job_post = translator.translate(data.job_post)

    # Translate address line-by-line
    if data.address:
        german_data.address = "\n".join([
            translator.translate(line.strip()) for line in data.address.strip().splitlines()
        ])

    # Translate bullet points
    german_data.bullet_points = translator.translate_batch(data.bullet_points)

    return german_data


def sanitize_filename(name: str, max_length: int = 30) -> str:
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', name.strip())
    return sanitized[:30]



def create_cover_letter_pdf(data: CoverLetterInput, lang: str = "en") -> str:
    base_dir = "src/agent/COVER_LETTERS"
    company_dir = sanitize_filename(data.company_name)
    job_file = sanitize_filename(data.job_post)
    if lang == "de":
        job_file += "_de"
    full_dir = os.path.join(base_dir, company_dir)
    os.makedirs(full_dir, exist_ok=True)
    file_path = os.path.join(full_dir, f"{job_file}.pdf")

    if lang == "de":
        translator = GoogleTranslator(source='auto', target='de')
        data = deepcopy(data)
        data.subject = translator.translate(data.subject)
        data.intro_paragraph = translator.translate(data.intro_paragraph)
        data.closing_paragraph = translator.translate(data.closing_paragraph)
        data.company_name = translator.translate(data.company_name) if data.company_name else None
        data.job_post = translator.translate(data.job_post)
        if data.address:
            data.address = "\n".join(translator.translate(line.strip()) for line in data.address.strip().splitlines())
        data.bullet_sections = translator.translate_batch(data.bullet_sections)

    margin_mm = 1.5 * 25.4
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=margin_mm,
        leftMargin=margin_mm,
        topMargin=margin_mm,
        bottomMargin=margin_mm,
    )

    styles = getSampleStyleSheet()
    if "CustomTitle" not in styles:
        styles.add(ParagraphStyle(name="CustomTitle", fontSize=16, leading=22, alignment=TA_CENTER, spaceAfter=12, fontName="Helvetica-Bold"))
    if "CustomHeader" not in styles:
        styles.add(ParagraphStyle(name="CustomHeader", fontSize=12, leading=14, alignment=TA_CENTER, spaceAfter=6, fontName="Helvetica-Bold"))
    if "CustomNormal" not in styles:
        styles.add(ParagraphStyle(name="CustomNormal", fontSize=11, leading=14, alignment=TA_LEFT, spaceAfter=6, fontName="Helvetica"))
    if "ContactLine" not in styles:
        styles.add(ParagraphStyle(name="ContactLine", fontSize=11, leading=14, alignment=TA_CENTER, spaceAfter=2, fontName="Helvetica", textColor="black"))
    if "ContactLinks" not in styles:
        styles.add(ParagraphStyle(name="ContactLinks", fontSize=11, leading=14, alignment=TA_CENTER, spaceAfter=12, fontName="Helvetica", textColor="blue", underline=True))
    if "CompanyNameLeft" not in styles:
        styles.add(ParagraphStyle(name="CompanyNameLeft", fontSize=12, leading=14, alignment=TA_LEFT, spaceAfter=6, fontName="Helvetica-Bold"))

    elements = []
    # elements.append(Paragraph("COVER LETTER" if lang == "en" else "BEWERBUNGSSCHREIBEN", styles["CustomTitle"]))
    elements.append(Paragraph(data.sender_name, styles["CustomHeader"]))
    elements.append(Paragraph(f"Braunschweig, Germany | +49 15510 030840", styles["ContactLine"]))

    links_html = (
        f'<a href="mailto:{data.email}">{data.email}</a> | '
        f'<a href="{data.github_url}">GitHub</a> | '
        f'<a href="{data.linkedin_url}">LinkedIn</a>'
    )
    elements.append(Paragraph(links_html, styles["ContactLinks"]))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(datetime.now().strftime("%d. %B %Y"), styles["CustomNormal"]))

    if data.company_name:
        elements.append(Paragraph(data.company_name, styles["CompanyNameLeft"]))

    if data.address:
        for line in data.address.split("\n"):
            elements.append(Paragraph(line.strip(), styles["CustomNormal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(data.subject, styles["CustomHeader"]))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(data.intro_paragraph, styles["CustomNormal"]))
    elements.append(Spacer(1, 8))

    bullet_items = [ListItem(Paragraph(bullet, styles["CustomNormal"])) for bullet in data.bullet_sections]
    elements.append(ListFlowable(bullet_items, bulletType="bullet"))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph(data.closing_paragraph, styles["CustomNormal"]))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Warm regards," if lang == "en" else "Mit freundlichen Grüßen,", styles["CustomNormal"]))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(data.sender_name, styles["CustomNormal"]))

    doc.build(elements)
    return file_path


    
@tool("cover-letter-pdf-generator", args_schema=CoverLetterInput, return_direct=True)
def generate_cover_letter_pdf_file(**kwargs) -> str:
    """
    Generate professional cover letter PDFs (English and German) based on input data.
    Saves the PDFs under src/agent/COVER_LETTERS/<sanitized_company>/<sanitized_job>.pdf.
    Returns the path to the English version.
    """
    data = CoverLetterInput(**kwargs)
    en_path = create_cover_letter_pdf(data, lang="en")
    _ = create_cover_letter_pdf(data, lang="de")
    return en_path


@tool("edit_cover-letter-pdf-generator", args_schema=CoverLetterInput, return_direct=True)
def edit_cover_letter_pdf_file(**kwargs) -> str:
    """
    Edit or overwrite existing cover letter PDFs (English and German) by regenerating them with new input.
    Returns the path to the updated English PDF file.
    """
    data = CoverLetterInput(**kwargs)
    en_path = create_cover_letter_pdf(data, lang="en")
    _ = create_cover_letter_pdf(data, lang="de")
    return en_path