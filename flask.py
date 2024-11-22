import streamlit as st
import google.generativeai as ai
from PIL import Image


st.image(r"C:\Users\anees\OneDrive\Pictures\Downloads\AI.jpeg")

# Set the API key directly
api_key1 = "AIzaSyAXQ2pvBuaCGp44SaUEgWYdpE_QPNdEOP4"
ai.configure(api_key=api_key1)

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only."""

# Initialize the model (check if `Generativemodel` is correct; it might vary)
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                            system_instruction=sys_prompt)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chatbot = model.start_chat(history=[])

st.title("Data Science Tutor Application")

# Collect user input
user_prompt = st.text_input("Enter your query", placeholder="I'm looking for details here...")

st.sidebar.title("Chat History")
if st.session_state.chat_history:
    for i, (role, text) in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"**{i + 1}. {role.capitalize()}**: {text}")

btn_click = st.button("Generate Answer")

if btn_click and user_prompt:
    # Generate the response
    response = model.generate_content(user_prompt)  # Confirm the correct method name here
    st.session_state.chat_history.append(("ai", response.text))
    st.write(response.text)
