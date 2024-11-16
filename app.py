import streamlit as st

st.set_page_config(page_title="ChatGPT")
st.title("Questions with our campus trees dataset?")

# st.write("Hello World")
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    # st.line_chart(np.random.randn(30, 3))


uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

from utils import get_answer_csv # type: ignore

if uploaded_file is not None:
    query = st.text_area("Ask any question related to the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer_csv(uploaded_file, query))


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")