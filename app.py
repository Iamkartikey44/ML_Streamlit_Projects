import streamlit as st
import openai

st.title("Readme Generator Wiht the help of ChatGPT")

upload_file = st.file_uploader("Upload Code File")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def ask_query(query):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response['choices'][0]['text']


if upload_file is not None:
    content = upload_file.read().decode()
    response = ask_query(f"{content}\n\nRead the code and generate a README.md for it in markdown format.")
    st.markdown("""----""")
    st.subheader("Response")
    st.text(response)
    st.markdown(""""----""")
    st.subheader("Preview")
    st.markdown(response)
