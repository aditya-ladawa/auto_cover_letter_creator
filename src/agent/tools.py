import os
import re
from fpdf import FPDF
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class CoverLetterInput(BaseModel):
    company_name: str = Field(description="Name of the company")
    job_post: str = Field(description="Role or job post title")
    address: Optional[str] = Field(default=None, description="Company address")
    city_state_country: Optional[str] = Field(default=None, description="City, state, and country of company")
    subject: str = Field(description="Subject line of the cover letter")
    salutation: str = Field(description="Salutation (e.g., Dear Hiring Manager)")
    body: str = Field(description="Body text of the cover letter with optional **bold** and [link](url) formatting")

def sanitize_name(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

class PDFWithLinks(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=False)
        self.add_font("Calibri", "", "Calibri/calibri.ttf", uni=True)
        self.add_font("Calibri", "B", "Calibri/calibri_bold.ttf", uni=True)
        self.set_font("Calibri", size=11)
        self.set_margins(15, 15, 15)
        self.add_page()
        self.max_height = self.h - self.b_margin

    def write_inline_text(self, text):
        self.set_text_color(0, 0, 0)
        self.set_font("Calibri", "", 11)
        self.multi_cell(0, 6, text)

    def write_styled_paragraph(self, paragraph):
        words = re.split(r'(\*\*.+?\*\*|\[.+?\]\(.+?\))', paragraph)
        for word in words:
            if word.startswith("**") and word.endswith("**"):
                text = word[2:-2]
                self.set_font("Calibri", "B", 11)
                self.set_text_color(0, 0, 0)
                self.write(self.font_size_pt / 2 + 1, text)
            elif word.startswith("[") and "](" in word and word.endswith(")"):
                label = re.search(r"\[(.*?)\]", word).group(1)
                link = re.search(r"\((.*?)\)", word).group(1)
                self.set_font("Calibri", "", 11)
                self.set_text_color(0, 0, 255)
                self.write(self.font_size_pt / 2 + 1, label, link)
            else:
                self.set_font("Calibri", "", 11)
                self.set_text_color(0, 0, 0)
                self.write(self.font_size_pt / 2 + 1, word)
        self.ln(8)


@tool("create_cover_letter", args_schema=CoverLetterInput, return_direct=True)
def create_cover_letter(
    company_name: str,
    job_post: str,
    address: Optional[str] = None,
    city_state_country: Optional[str] = None,
    subject: str = "",
    salutation: str = "",
    body: str = "",
) -> str:
    """
    Generate a cover letter PDF with styled text and hyperlinks, limited to one page.
    Saves to src/agent/COVER_LETTERS/{company}/{company}_{job_post}_cover_letter.pdf
    """
    sanitized_company = sanitize_name(company_name)
    sanitized_post = sanitize_name(job_post)
    dir_path = os.path.join("src", "agent", "COVER_LETTERS", sanitized_name)

    os.makedirs(dir_path, exist_ok=True)
    pdf_path = os.path.join(dir_path, f"{sanitized_company}_{sanitized_post}_cover_letter.pdf")

    pdf = PDFWithLinks()

    # Header
    header_lines = [
        "Aditya Ladawa Braunschweig, Germany | ",
        "adityaladawa12@gmail.com",
        " | +49 15510 030840 | ",
        "GitHub",
        " | ",
        "LinkedIn"
    ]
    links = {
        "adityaladawa12@gmail.com": "mailto:adityaladawa12@gmail.com",
        "GitHub": "https://github.com/aditya-ladawa",
        "LinkedIn": "https://www.linkedin.com/in/aditya-ladawa/"
    }

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Calibri", "", 11)

    for item in header_lines:
        if item in links:
            pdf.set_text_color(0, 0, 255)
            pdf.set_font("Calibri", "", 11)
            pdf.cell(pdf.get_string_width(item), 6, item, ln=0, link=links[item])
        else:
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("Calibri", "", 11)
            pdf.cell(pdf.get_string_width(item), 6, item, ln=0)
    pdf.ln(10)

    # Date
    pdf.set_text_color(0, 0, 0)
    date_str = datetime.now().strftime("%d. %B %Y")
    pdf.cell(0, 6, date_str, ln=True)
    pdf.ln(5)

    # Company Info
    pdf.cell(0, 6, company_name, ln=True)
    if address:
        pdf.cell(0, 6, address, ln=True)
    if city_state_country:
        pdf.cell(0, 6, city_state_country, ln=True)
    pdf.ln(4)

    # Subject
    if subject:
        pdf.set_font("Calibri", "B", 11)
        pdf.cell(0, 6, subject, ln=True)
        pdf.set_font("Calibri", "", 11)
        pdf.ln(6)

    # Salutation
    if salutation:
        pdf.cell(0, 6, salutation + ",", ln=True)
        pdf.ln(4)

    # Body
    for paragraph in body.strip().split("\n\n"):
        if pdf.get_y() > pdf.max_height - 15:
            break
        pdf.write_styled_paragraph(paragraph.strip())

    # Signature
    pdf.ln(4)
    pdf.cell(0, 6, "Sincerely,", ln=True)
    pdf.cell(0, 6, "Aditya Ladawa", ln=True)

    pdf.output(pdf_path)
    return pdf_path
