
# pip install streamlit
# pip install bardapi
# pip install dotenv
# pip install --upgrade protobuf==3.19.0

#pip install utils
# import os
import streamlit as st
from PIL import Image
import utils as utl
import os


#SIDEBAR AND OPTIONS

option = st.sidebar.radio(
        "Select an Application", ('Chat With Your Data','Image Analysis',)
    )

#CHAT WITH BARD
if(option == 'Chat With Your Data'):
    st.markdown(" <h1 style='text-align: center;margin-left:-24px;font-size:1.8rem; margin-top:-24px;color:#694bfd; font-family: Source sans pro,sans-serif !important;' ></h1>", unsafe_allow_html=True)
    from bardapi import Bard
    from dotenv import load_dotenv

    load_dotenv()

    def call_bard(query):
            # Replace 'YOUR_API_KEY' with your actual Bard API key
            bard = Bard(token="fAjNhuslL1hUIIU90BDdLXY3Wgls1MPQ7RSLCBHIvH1WW7ykpUAaRGj7Xdf92PkmgwIoUg.")
            answer = bard.get_answer(query)
            return answer['content']

    def main():

            # Get user input through a text input box
            query = st.text_input("Ask a question:")

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

#IMAGE ANALYSIS

if(option == 'Image Analysis'):
    st.markdown(" <h1 style='text-align: center;margin-left:-24px;font-size:1.8rem; margin-top:-24px;color:#694bfd; font-family: Source sans pro,sans-serif !important;' ></h1>", unsafe_allow_html=True)
    from bardapi import Bard

        # Replace 'YOUR_API_KEY' with your actual Bard API key
    BARD_API_KEY = "fAjNhuslL1hUIIU90BDdLXY3Wgls1MPQ7RSLCBHIvH1WW7ykpUAaRGj7Xdf92PkmgwIoUg."

    def call_bard_for_image(query, image):
            bard = Bard(token=BARD_API_KEY)
            answer = bard.ask_about_image(query, image)
            return answer['content']

    def main():
            st.title("Bard API Image Analysis")

            # File uploader for image
            uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

            # Get user input through a text input box
            query = st.text_input("Ask a question")

            if st.button("Analyze Image"):
                if uploaded_file and query:
                    # Read the image file
                    image = uploaded_file.read()

                    # Call Bard API with the user's query and the uploaded image
                    response = call_bard_for_image(query, image)
                    
                    # Display the Bard's answer
                    st.write("Bard's Answer:")
                    st.write(response)
                else:
                    st.warning("Please upload an image and enter a question.")

    if __name__ == "__main__":
            main()







