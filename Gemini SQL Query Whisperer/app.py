# 🌟🤖 Unleashing Gemini: The SQL Query Whisperer! 📚🔍

# Summoning the required enchantments 🧙📜
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Activating the mystical environment variables 🔮🌐
load_dotenv()

# Setting up Streamlit page configuration 🛠️📝
st.set_page_config(page_title="I can Retrieve Any SQL query")

# Configuring the cosmic powers of Gemini 🌌🔑
st.title("Welcome to Gemini: Your SQL Query Oracle! 🧙📜")
st.subheader("Are you ready to summon the powers of the SQL realm? Let's begin our quest!")

# Prompting for API key 🔑👀
api_key = st.text_input("Enter your Google API Key:", type="password")

# If API key provided, configure Gemini 🤖🛠️
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    genai.configure(api_key=api_key)

## Function to summon the wisdom of OpenAI model and decipher the queries

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    print(response.text)
    output = read_sql_query(response.text, "test.db")
    print(output)
    return output

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

## Initializing the magical Streamlit app
prompt = [
  """You possess mastery in translating English inquiries into SQL commands! The SQL database, dubbed STUDENT, boasts columns such as NAME, CLASS, and SECTION. For instance, consider this query: 'Example 1 - How many entries of records are present?' The corresponding SQL command would resemble: 'SELECT COUNT(*) FROM STUDENT;' Additionally, ensure that the SQL code does not contain ``` at the beginning or end, and 'sql' should appear in the output.
    """
]

questions = st.text_input("Enter your magical SQL question here: ", key="input")

submit = st.button("Summon the Answer!")

## If the magical button is clicked
if submit:
    
    response = get_gemini_response(questions, prompt)
    st.subheader("Behold! The Oracle Speaks:")
    for row in response:
        print(row)
        st.subheader(row)
