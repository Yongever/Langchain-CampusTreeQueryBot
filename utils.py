# type: ignore
import os
from typing import TextIO

import openai
import pandas as pd
import streamlit as st
# from langchain_experimental.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI

# openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_answer_csv(file: TextIO, API_KEY, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """
    # Load the CSV file as a Pandas dataframe
    #df = pd.read_csv(file)
    #df = pd.read_csv("titanic.csv")

    llm = OpenAI(openai_api_key=API_KEY, temperature=0)

    # Create an agent using OpenAI and the Pandas dataframe
    agent = create_csv_agent( llm, file, verbose=True, allow_dangerous_code=True)
    #agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    # Run the agent on the given query and return the answer
    #query = "whats the square root of the average age?"
    answer = agent.run(query)
    
    return answer
