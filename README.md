# Bard
Bard API integration using Cookie value 
Google Bard haven't released Bard API to integrate Bard completely so i have integrated the Bard API using the cookie value
I used streamlit package to create the frontend to deploy the bard functionality
#how to to get cookie value from your bard website
step 1:press F12 
step 2:click >> arows and goto Applications
step 3:go to cookies and click __Secure-1PSID and copy the value given below and paste it the code
#Here i uploaded two files one is Bard.py and streamlit.py 

#I have only integrated the text functionality of the bard in Bard.py file
#if you need to integrate the image use below code to integrate the image functionality from bard

def call_bard_for_image(query, image):
    bard = Bard(token=BARD_API_KEY)
    answer = bard.ask_about_image(query, image)
    return answer['content']
query = st.text_input("Ask Bard about the image:")
 image = uploaded_file.read()
            response = call_bard_for_image(query, image)
#To integrate in streamlit use the below code in streamlit.py file replace the existing functions of text with above code
#to run streamlit.py file go anaconda prompt and install bardapi and streamlit package and update pip install --upgrade protobuf==3.20.0 and go to the directory where you have saved the streamlit.py file and run the command python -m streamlit run file_nume.py

