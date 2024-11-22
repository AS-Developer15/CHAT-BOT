import streamlit as st
import google.generativeai as genai

# Gemini ka Code
keyVar="AIzaSyDIUAnyr3-Z67AOlfP0b7Ypku1wBFyEX20"
genai.configure(api_key=keyVar)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit Code
st.title("Gemini Clone")
st.write("Gemini Clone stimulates real life conversation and answers to your prompts in a real life conversative manner. Our bot uses a combination of artificial intelligence (AI) and natural language processing (NLP) techniques to understand and respond to user queries. ")
st.write("All rights reserved to @AS.Developer")
st.divider()
# Result Function
def replyFunc(userPrompt:str):   
    response = model.generate_content(f"Reply to the prompt of '{userPrompt} '. ")
    return response.text

st.chat_message("assistant").markdown("Hello, what is in your mind?")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response= replyFunc(prompt)
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})        
