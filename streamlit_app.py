import streamlit as st
import requests
import datetime

import sys

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Travel Planner Agentic Application", 
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("Travel Planner Agentic Application")

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat history

st.header("How can I help you in planning a trip? Let me know where do you want to visit.")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="e.g. Plan a trip to New York")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        # Show user input in chat history
        # Show thinking spinner while waiting for response
        with st.spinner("Thinking..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned")
            markdown_contemt = f"""# AI Travel Plan
            # **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            # **Question:** {user_input}

            ----

            {answer}
            

            ----

            *** Note**: This is a simulated Travel Plan from the AI model. Please verify all information, especially prices, operating hours, and travel requirements before your trip *
            
            """
            st.markdown(markdown_contemt)
        else:
            st.error("Bot is not responding. Please try again later. "+ response.text)

    except Exception as e:
        raise f"The response failed due to {e}"
    
    

    st.session_state.messages.append({"role": "user", "content": user_input})
    response = requests.post(f"{BASE_URL}/chat", json={"messages": st.session_state.messages})
    
    if response.status_code == 200:
        bot_response = response.json().get("response", "")
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
    else:
        st.error("Error: Unable to get a response from the server.")