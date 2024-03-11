## 🤖📚 Jovial Q&A Chatbot: Your Comedian AI Assistant 🎭🎤

import streamlit as st
import os

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

## Streamlit UI 🖥️🎨
st.set_page_config(page_title="Jovial Q&A Chatbot")
st.title("Hey, Let's Chat! 🗣️🤖")

from dotenv import load_dotenv
load_dotenv()

# Prompting for API key 🔑👀
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# If API key provided, configure the chatbot 🤖🛠️
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    chat = ChatOpenAI(temperature=0.5)

    if 'flowmessages' not in st.session_state:
        st.session_state['flowmessages']=[
            SystemMessage(content="You're about to enter a world of laughter with our Comedian AI Assistant! 😄🤖")
        ]

    ## Function to summon the witty responses from our AI assistant
    def get_chatmodel_response(question):

        st.session_state['flowmessages'].append(HumanMessage(content=question))
        answer = chat(st.session_state['flowmessages'])
        st.session_state['flowmessages'].append(AIMessage(content=answer.content))
        return answer.content

    input_question = st.text_input("Enter your question here: ", key="input")
    response = get_chatmodel_response(input_question)

    submit = st.button("Ask Away! 🚀🎤")

    ## If the magic button is clicked
    if submit:
        st.subheader("Here's the Funny Response:")
        st.write(response)
