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

from agent.tools import create_cover_letter
from agent.prompts import aditya_text, resume_text




configurable = Configuration()


llm = init_chat_model(model=configurable.model, model_provider=configurable.model_provider, temperature=0.0)



llm_prompt = f"""
Given the job and company information, you should draft an impressive cover letter which would get user the interviews.
Today's dat: {datetime.now().strftime("%d. %B %Y")}
Here is information about me:
{aditya_text}

Here is my resume and additional information needed to craft a best cover letter which would get me a job:
{resume_text}



"""
graph = create_react_agent(model=llm, tools=[create_cover_letter], prompt=llm_prompt)

