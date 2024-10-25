import streamlit as st
from openai import OpenAI
import mmap
import os

def load_model_memory_mapped(model_path):  # New function
    """Loads a model using memory mapping."""
    try:
        with open(model_path, "r+b") as f:
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            return mm # Return the mmap object

    except Exception as e:
        print(f"Error memory mapping model: {e}")
        return None

def run_chatbot(user_input, port=8080,
                instructions="You are a helpful AI assistant.", 
                model_path=None):
    """Runs chatbot."""
    try:
        client = OpenAI(
            base_url=f"http://localhost:{port}/v1",
            api_key="sk-no-key-required"
        )

        if model_path:
            mm = load_model_memory_mapped(model_path)
            if mm:
                try:

                    completion = client.chat.completions.create(
                        model="LLaMA_CPP", # Correct model identifier
                        messages=[
                            {"role": "system", "content": instructions},
                            {"role": "user", "content": user_input}
                        ]
                    )
                finally:
                    mm.close() # Always close the mmap object
        else:
            completion = client.chat.completions.create(
                model="LLaMA_CPP",
                messages=[
                    {"role": "system", "content": instructions},
                    {"role": "user", "content": user_input}
                ]
            )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred."
    
def initialize_session_state():
    """Initializes session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "turn_count" not in st.session_state:
        st.session_state.turn_count = 0

def add_message(role, content):
    """Adds a message to the chat history."""
    st.session_state.messages.append({"role": role,
                                      "content": content})
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
            st.markdown(f"Chatbot: {message['content']}",
                        unsafe_allow_html=True)

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
model_paths = {  # For memory mapping
    "TinyLlama":
    "llamafile/TinyLlama-1.1B-Chat-v1.0.F16.llamafile",
    "Rocket":
    "llamafile/rocket-3b.Q5_K_M.llamafile",
    "Other": ""  # Placeholder for other models
}
selected_model = st.selectbox("Select Model:", list(model_paths.keys()))
if selected_model == "Other": # If other is selected
    model_path_other = st.text_input("Enter path to Other Model:", "")
    if not model_path_other or not os.path.exists(model_path_other):
        st.error("Invalid path for Other Model.")
        st.stop()

    port = st.text_input("Enter Port for Other Model:", "8082")
elif selected_model != "Other":
    ports = {"TinyLlama": "8080", "Rocket": "8081"}
    port = ports[selected_model]  # Get predefined port


# Memory Mapping Option
use_mmap = st.checkbox("Use Memory Mapping (if supported)", value=False)
st.session_state.use_mmap = use_mmap


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
                    # Determine model_path
                    if selected_model == "Other":
                        model_path = model_path_other
                    elif st.session_state.use_mmap:
                         model_path = model_paths.get(selected_model)
                    else:
                        model_path = None

                    response = run_chatbot(user_input, port,
                                           st.session_state.instructions, model_path)
                    add_message("assistant", response)

        display_chat_history()