import streamlit as st
from openai import OpenAI
import time

def run_chatbot(user_input, port, instructions):
    """Runs the chatbot."""
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
    """Initializes session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "turn_count" not in st.session_state:
        st.session_state.turn_count = 0

def add_message(role, content):
    """Adds a message to the chat history."""
    st.session_state.messages.append({"role": role, "content": content})
    st.session_state.turn_count += 1


def display_chat_history():
    """Displays and allows download of chat history."""
    chat_history_text = ""
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_history_text += f"You: {message['content']}\n"
            st.write(f"You: {message['content']}")
        else:
            chat_history_text += f"Chatbot: {message['content']}\n"
            st.markdown(f"Chatbot: {message['content']}", unsafe_allow_html=True)

    st.download_button(
        label="Download Chat History",
        data=chat_history_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )

# --- Main Streamlit App ---
st.title("Chat with LLaMA")

initialize_session_state()


# Model Selection
ports = {"TinyLlama": "8080", "Rocket": "8081", "Other": ""}  # Example
selected_model = st.selectbox("Select Model:", list(ports.keys()))
port = ports[selected_model]
if selected_model == "Other":
    port = st.text_input("Enter Port for Other Model:", "8082")


instructions = st.text_area("Custom system instructions (blank is default):",
                            "You are a helpful AI assistant.")


if st.button("Start Chat"):
    if not port:
        st.error("Please select a model or enter a port.")
    else:
         st.session_state.instructions = instructions
         st.session_state.port = port


if "instructions" in st.session_state and "port" in st.session_state:
    try:
        port = int(st.session_state.port)
    except ValueError:
        st.error("Invalid port number. Please enter a valid integer.")
        del st.session_state.port # Clear invalid port
    else:

        st.write(f"Turn Count: {st.session_state.turn_count}")


        user_input = st.text_input("You: ", "")
        if st.button("Send"):
            if user_input:
                with st.spinner("Thinking..."):
                    add_message("user", user_input)
                    response = run_chatbot(user_input, port, st.session_state.instructions)
                    add_message("assistant", response)


        display_chat_history()