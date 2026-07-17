import streamlit as st
from openai import OpenAI
#_____________________________________________________________________
# Page Config

st.set_page_config(
    page_title="Sravani Mini ChatGPT - Mistral",
    page_icon="🤖",
    layout="centered")
st.title("🤖 Sravani Mini ChatGPT (Mistral AI)")
#_____________________________________________________________________
# API Key
api_key = "r1Myxm8iW5DYfdg3rKThwXcg3rg3djLU"

#_____________________________________________________________________
# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."}]
#_____________________________________________________________________
# Show Previous Messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#_____________________________________________________________________
# Chat Input
prompt = st.chat_input("Type your message...")
if prompt:
    if not api_key:
        st.error("Please enter your Mistral API Key.")
        st.stop()

    client = OpenAI(api_key=api_key,
        base_url="https://api.mistral.ai/v1")
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt})

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="mistral-small-latest",
                messages=st.session_state.messages)
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply})
#_____________________________________________________________________
# Sidebar
with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI"}]
        st.rerun()
    st.markdown("---")
    st.write("**Model:** mistral")