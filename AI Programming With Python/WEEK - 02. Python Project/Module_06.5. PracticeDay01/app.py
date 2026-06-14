import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

st.title(" :streamlilt: Streamlit Practice Apps")
st.divider()


st.header(" :star: 1. Calculator")
numbers = list(map(int, st.text_input("Enter two numbers").split()))
operation = st.selectbox("Select Operation", ["+", "-", "*", "/"])
button1 = st.button("Calculate")
if button1:
    if operation == "+": 
        result = numbers[0] + numbers[1]
    elif operation == "-":
        result = numbers[0] - numbers[1]
    elif operation == "*":
        result = numbers[0] * numbers[1]
    elif operation == "/":
        if numbers[1] != 0:
            result = numbers[0] / numbers[1]
        else:
            result = "Error: Division by zero"
            
    st.write(f"Result: {result}")

else:
    st.warning("Please enter numbers and select an operation to calculate.")

st.divider()



st.header(" :star: 2. GEMINI_PRO")
api_key=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = st.text_input("Enter your prompt for GEMINI_PRO")
button2 = st.button("Generate")

if button2:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    st.markdown(response.text)

st.divider()


st.header(" :star: 3. GEMINI_PRO with Improved Sentence")
promot = st.text_input("Enter Your Sentence : ")
button3 = st.button("Improve")
if button3:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Improve this sentence professionally in a single sentence: {promot}"
    )
    st.markdown(response.text)