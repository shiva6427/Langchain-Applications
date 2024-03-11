# 🌟🍔🥗 Unveiling Gemini: Your AI Nutritionist 🥦🔍

# Importing necessary libraries 📚🔍
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Loading environment variables 🛠️🔑
load_dotenv()

# Function to fetch response from Gemini AI 🤖🗣️
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to process uploaded image 📸🖼️
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("Oops! Looks like you forgot to upload an image. No worries, we'll just imagine your delicious food for now. 🍔🥗")

# Initialize Streamlit app 🚀🎨
st.set_page_config(page_title="Gemini Image Demo")

# Setting up Streamlit app 🛠️📝
st.markdown("<h1 style='text-align: center; color: #FFA500;'>Welcome to Gemini 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #F00000;'>Your AI Nutritionist! 🍽️</h2>", unsafe_allow_html=True)
st.subheader("Are you prepared to unravel the mysteries concealed within your meal? Let us delve into it!🍔🔍")

# Prompting for API key 🔑👀
api_key = st.text_input("Enter your Google API Key:", type="password")

# If API key provided, configure Gemini 🤖🛠️
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    genai.configure(api_key=api_key)

# Taking input prompt and image file from user 📝📸
input = st.text_input("What would you like to uncover about your food? ", key="input")
uploaded_file = st.file_uploader("Choose an image of your food...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Mmm... Delicious!", use_column_width=True)

# Button to trigger Gemini response 🚀🔮
submit = st.button("Unravel the Mysteries!")

# Prompt to guide the user on what to input 📝🔍
input_prompt = """
               Ready to take the plunge into the world of nutrition expertise? Describe the delectable delights in the image, and let Gemini do its magic!
               Remember to list each food item along with its calorie count, like a true food whisperer:

               1. Burger - 500 calories
               2. Salad - 100 calories
               ----
               ----
               """

# If submit button is clicked 🖱️🚀
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Drumroll, please... 🥁✨")
    st.write("The culinary oracle, Gemini, has spoken: ")
    st.write(response)
