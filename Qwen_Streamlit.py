import streamlit as st
import requests
import json

def query_ollama(model, system_prompt, user_prompt):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "system": system_prompt,
        
        "prompt": user_prompt
    }
    
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        response_text = response.text
        lines = response_text.strip().split("\n")
        full_response = "".join(json.loads(line)["response"] for line in lines)
        return full_response
    else:
        return f"Error {response.status_code}: {response.text}"

st.title("Ollama Chatbot")


model = 'qwen2.5:0.5b'
system_prompt = "You are a helpful AI assistant that generates clean and well-commented Python code."
user_prompt = st.text_area("User Prompt", "Please Enter prompts to generate response")

if st.button("Generate Response"):
    if user_prompt.strip():
        with st.spinner("Generating response..."):
            response = query_ollama(model, system_prompt, user_prompt)
            st.text_area("Response", response, height=500)
    else:
        st.warning("Please enter a user prompt.")