import streamlit as st
from openai import OpenAI

def run_chatbot(user_input):
    """Runs the chatbot, sending user input to the llamafile 
    model and returning the response."""
    try:
        client = OpenAI(
            base_url="http://localhost:8080/v1",  
            api_key="sk-no-key-required" 
        )

        completion = client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input} 
            ]
        )
        response = completion.choices[0].message.content
        return response

    except Exception as e:
        return f"An error occurred: {e}"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chat with LLaMA")

# User input
user_input = st.text_input("You: ", "")
if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = run_chatbot(user_input)
        # Append chatbot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.markdown(f"Chatbot: {message['content']}", unsafe_allow_html=True)
