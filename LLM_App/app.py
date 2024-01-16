from dotenv import load_dotenv
load_dotenv() ##Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to load Gemini Pro Model and Get Responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## Initialize streamlit App

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the Question")

## When Submit is Clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)


