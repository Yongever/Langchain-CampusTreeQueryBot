# Question answering system over SQL & CSV data

## Motivation
This web app aims to make complex environmental data accessible to all by utilizing GPT-3.5 to translate natural language queries into SQL or Pandas queries. Hosted on GitHub and built with Langchain and Streamlit, the app uses a dataset from Dr. Binney Girdler Kiah at Kalamazoo College about campus trees, detailing their health and carbon sequestration. It serves as an educational tool for users without a technical background, allowing easy interaction with scientific data and supporting sustainability initiatives on campus. Future developments hope to integrate dynamic data updates for real-time analysis, enhancing its utility for environmental research and education.


## Architecture

At a high-level, the steps of these systems are:

1. Convert question to SQL query: Model converts user input to a SQL query.

2. Execute SQL query: Execute the query.

3. Answer the question: Model responds to user input using the query results.

Note that querying data in CSVs can follow a similar approach

<img width="831" alt="image" src="https://github.com/user-attachments/assets/d52c7ed7-54ac-436a-99f0-3d085bb9fd14">



If you don't want to use a local development environment, Streamlit Community Cloud makes it easy to create a GitHub codespace that's fully configured for Streamlit app development.

This is an example made through Streamlit Community Cloud:

https://question-answering-system-over-sql-data-extewqnrum5foh8ahnycbr.streamlit.app 

<img width="729" alt="image" src="https://github.com/user-attachments/assets/dca703ec-1cf3-401e-8f03-3bf1a1f16602">




Example after some prompts

<img width="720" alt="image" src="https://github.com/user-attachments/assets/fb2e18b4-2fef-4b50-8366-65fec5f4846b">
