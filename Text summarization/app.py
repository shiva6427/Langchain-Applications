## 🧠📝 Mindblowing PDF Summarizer: Unleash the Power of Langchain! 🚀🎉

import os
import streamlit as st
import PyPDF2
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Setting up the Streamlit UI 🖥️🎨
st.set_page_config(page_title="Mindblowing PDF Summarizer")
st.title("Welcome to the Mindblowing PDF Summarizer! 🧠📝")

# Prompting for OpenAI API key 🔑👀
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# If API key provided, configure the text summarizer 🤖🛠️
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    llm = ChatOpenAI(model_name='gpt-3.5-turbo')

    # System message
    system_message = SystemMessage(content="Welcome to the PDF Summarizer! 📝 Let's summarize some PDFs!")

    # Display system message
    st.write(system_message.content)

    # File uploader for PDF 📄🚀
    pdf_file = st.file_uploader("Upload a PDF file for summarization:", type=["pdf"])

    # Button to initiate summarization
    summarize_button = st.button("Summarize PDF 🚀")

    # If PDF uploaded and button clicked
    if pdf_file and summarize_button:
        try:
            # Extract text from PDF file
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ""
            for page_number in range(len(pdf_reader.pages)):
                pdf_text += pdf_reader.pages[page_number].extract_text()

            # Split PDF text into lines
            pdf_lines = pdf_text.split('\n')

            # Human message for summarization
            human_message = HumanMessage(content=pdf_text)

            # Chat messages to initiate conversation
            chat_messages = [system_message, human_message]

            # Function to retrieve summarized content
            def get_summarized_content():
                return llm(chat_messages).content

            # Fetching the summarized content
            summarized_content = get_summarized_content()

            # Displaying the summarized content
            st.subheader("Here's the Summarized PDF Content:")
            st.write(summarized_content)

        except Exception as e:
            st.error(f"An error occurred: {e}")
