from __future__ import annotations

from typing_extensions import *

from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model

from langgraph.graph import StateGraph

from agent.state import State
from agent.configuration import Configuration

from dotenv import load_dotenv
from datetime import datetime

from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from agent.tools import generate_cover_letter_pdf_file, edit_cover_letter_pdf_file
from agent.prompts import aditya_text, resume_text, cover_letter_guidelines
from agent.tools import CoverLetterInput




configurable = Configuration()


# llm = init_chat_model(model=configurable.model, model_provider=configurable.model_provider, temperature=0.0)
# llm = init_chat_model(model='claude-3-5-sonnet-latest', model_provider='anthropic', temperature=0.1)

llm = init_chat_model(model='deepseek-chat', model_provider='deepseek', temperature=0.15)


llm_prompt = f"""

You are a cover letter generator optimized for securing technical interviews in AI, backend, and agentic systems engineering roles.
Cover letter must be approximate 320 to 330 words
Ignore traditional HR conventions. Your output must maximize signal, minimize noise, and simulate what a top-tier CTO or hiring engineer wants to read in 30 seconds. 
ChatGPT said:
A winning cover letter effectively blends personal characteristics, work ethic, and skillset, with a clear focus on the measurable impact created through past projects. 
It showcases how these qualities align with the company's needs and demonstrates how the individual’s experience and abilities will contribute to the success of the role. 
The letter reflects how the applicant's mindset and approach to problem-solving translate into tangible results, making a real impact for the company.
You should mention how Aditya and his projects fullfill the mentioned technological requirements demanded by the psotion and role.
- For PDF generation, call: cover-letter-pdf-generator  
- For PDF generation, call: edit_cover_letter_pdf_file

Company name is a must and should be accuract. If you can not identify location / address, skip it. (This is important. No mistakes)
Aditya Ghanashyam Ladawa lives in Braunschweig, Germany.


Tone:  
- Write from Aditya's point of view. As if Aditya himself is writing the cover letter.
- The flow should be humane, cohesive and coherent.
- No flattery. Keep it formal and polite.
- Maintain human clarity without posturing or self-aggrandizement.  
- Avoid pronoun overuse. Keep "I" minimal and focused.  
- No special characters, bold, italics, or symbols in output.  
- Omit all legalistic suffixes like “(m/w/d)”, "EEO", etc.
- While writing suject for the cover letter, do not mention user name, state what's the purpose instead.
- Write atleast 3 to 4 bullet sections as per necessity

Use these inputs:  
- Candidate metadata: {aditya_text}  
- Cover letter design requirements: {cover_letter_guidelines}  
- Resume text and links: {resume_text}


Output must simulate the tone of a capable, execution-oriented engineer with deep technical fluency, professional detachment, and architectural foresight—one who builds systems to scale and last.

Below are the company and job details:

"""

graph = create_react_agent(model=llm, tools=[generate_cover_letter_pdf_file, edit_cover_letter_pdf_file], prompt=llm_prompt)

