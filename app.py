import streamlit as st
import google.generativeai as ai


# Set the page configuration
st.set_page_config(page_title="AI Code Reviewer")

api_key = st.secrets["GOOGLE_API_KEY"]
ai.configure(api_key=api_key)

sys_prompt = """You are an AI code Reviewer. 
                create a heading named Code Review where you should analyze the submitted code and identify potential bugs, errors, or areas of improvement in details.
                and another heading named Fixed Code where you should also provide the fixed code snippets.
"""

model = ai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                          system_instruction=sys_prompt)

st.title(":speech_balloon: An AI Code Reviewer")



# Initialize session state for storing user input history
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar for displaying input history
st.sidebar.title("User Input History")
if st.session_state.history:
    for idx, prompt in enumerate(st.session_state.history, 1):
        st.sidebar.write(f"{idx}. {prompt}")
else:
    st.sidebar.write("No history yet.")

# Multi-line input area for the user to type their query
user_prompt = st.text_area("Enter your query:", placeholder="Type your query here...")

btn_click = st.button("Generate Answer")

if btn_click and user_prompt:
    # Add user input to history
    st.session_state.history.append(user_prompt)

    # Generate response using the model
    response = model.generate_content(user_prompt)
    
    # Display the AI's response
    st.write(response.text)

