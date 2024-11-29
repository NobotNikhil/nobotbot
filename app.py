from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = henai.GenerativeModel("gemini-flash-1.5")
model = genai.GenerativeModel("gemini-pro")
def my_output(query) -> str:
    response = model.generate_content(query)
    return response.text


#### UI Development using streamlit
st.set_page_config(page_title="NOBOT'S_BOT")
st.header("NOBOT'S_BOT")
input = st.text_input("Input " , key = "input")
submit = st.button("Press me ;)")

if submit :
    response = my_output(input)
    st.subheader("Don't ask me this shit questions again->")
    st.write(response)