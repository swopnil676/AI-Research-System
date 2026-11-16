import streamlit as st
from langchain.agents import create_agent
# from langchain_mistralai import ChatMistralAI/
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url
from dotenv import load_dotenv

load_dotenv()

# model setup
# llm = ChatMistralAI(
#     model="ministral-8b-latest",
#     temperature=0
# )
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=st.secrets["GROQ_API_KEY"],
    temperature=0,
    max_retries=2
)

# 1st agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

# 2nd agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )


# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

    Topic: {topic}

    Research Gathered:
    {research}

    Structure the report as:
    - Introduction
    - Key Findings (minimum 3 well-explained points)
    - Conclusion
    - Sources (list all URLs found in the research)

    Be detailed, factual and professional."""),
])
writer_chain = writer_prompt | llm | StrOutputParser()


# critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a strict, unbiased and professional research evaluator.

    Your job is to evaluate each research report independently.
    Never give the same score by default.
    Do not be generous. Do not assume the report is good.

    Use this scoring rubric:

    9-10: Excellent, detailed, accurate, well-supported research.
    7-8: Good research, but some important details are missing.
    5-6: Average research with limited depth or weak explanations.
    3-4: Poor research with major gaps and unsupported claims.
    1-2: Very poor, incomplete or largely irrelevant research.

    Evaluate these factors:
    1. Accuracy and factual reliability.
    2. Depth of research.
    3. Quality of key findings.
    4. Supporting evidence and sources.
    5. Structure and clarity.

    Give a score based on the actual report, not a predetermined score.
    """),
    ("human", """Review the research report below and evaluate it strictly.

    Report:
    {report}

    Respond in this exact format:

    Score: X/10

    Strengths:
    - ...
    - ...

    Areas to Improve:
    - ...
    - ...

    One line verdict:
    ..."""),
])
critic_chain = critic_prompt | llm | StrOutputParser()
