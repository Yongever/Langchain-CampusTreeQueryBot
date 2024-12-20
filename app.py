import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="ChatGPT")
# st.title("💬Questions with our campus trees dataset?")




# Show title and description.
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses."
)
st.write(
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

openai_api_key = st.text_input("OpenAI API Key", type="password")
# OPENAI_API_KEY=openai_api_key
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")




if openai_api_key:
    from utils import get_answer_csv # type: ignore
    uploaded_file = "./original_campustrees.csv"
    query = st.text_area("Ask any question related to the dataset")
    st.write(get_answer_csv(uploaded_file, openai_api_key, query))



# uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])
# if uploaded_file is not None:
#     query = st.text_area("Ask any question related to the document")
#     button = st.button("Submit")
#     if button:
#         st.write(get_answer_csv(uploaded_file, query))




# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
if openai_api_key:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("Any following questions?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})





# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
