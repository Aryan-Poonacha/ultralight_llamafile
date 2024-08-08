import streamlit as st
from openai import OpenAI

def run_chatbot(user_input, port, instructions):
    """Runs the chatbot, sending user input
    to the LLaMA model and returning the response."""
    try:
        client = OpenAI(
            base_url=f"http://localhost:{port}/v1",  
            api_key="sk-no-key-required" 
        )

        completion = client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": user_input} 
            ]
        )
        response = completion.choices[0].message.content
        return response

    except Exception as e:
        return f"An error occurred: {e}"

def initialize_session_state():
    """Initializes the chat history in session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role, content):
    """Adds a message to the chat history in session state."""
    st.session_state.messages.append({"role": role, "content": content})

def display_chat_history():
    """Displays the chat history from session state."""
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"You: {message['content']}")
        else:
            st.markdown(f"Chatbot: {message['content']}", unsafe_allow_html=True)

# --- Main Streamlit App ---
st.title("Chat with LLaMA")

initialize_session_state()

instructions = st.text_input("Custom system instructions (blank is default):",
                             "You are a helpful AI assistant.")
port = st.text_input("Enter port no of local server (default=8080):",
                     "8080")

if st.button("Start Chat"):
    st.session_state.instructions = instructions
    st.session_state.port = port

if "instructions" in st.session_state and "port" in st.session_state:
    try:
        port = int(st.session_state.port)
    except ValueError:
        st.error("Invalid port number. Please enter a valid integer.")
    else:
        user_input = st.text_input("You: ", "")
        if st.button("Send"):
            if user_input:
                add_message("user", user_input)
                response = run_chatbot(user_input, port, st.session_state.instructions)
                add_message("assistant", response)

        display_chat_history()
