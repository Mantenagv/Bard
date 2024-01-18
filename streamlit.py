import streamlit as st
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

def call_bard(query):
    # Replace 'Your_cookie_value' with your actual Bard API key
    bard = Bard(token="Your_cookie_value")
    answer = bard.get_answer(query)
    return answer['content']

def main():
    st.title("Bard API Streamlit App")

    # Get user input through a text input box
    query = st.text_input("Ask Bard a question:")

    if st.button("Get Answer"):
        if query:
            # Call Bard API with the user's query
            response = call_bard(query)
            st.write("Bard's Answer:")
            st.write(response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()