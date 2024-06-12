import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import google.generativeai as genai
#Enter your API key here
genai.configure(api_key='Enter your API key here')
#configure the gemini models required
model = genai.GenerativeModel('gemini-pro')

#The function that is being used to generate the response from the text inputs via API
def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text

#Function to get the input text from the user
def get_text():
    input_text=st.text_input("Message Here!",key='input')
    return input_text


st.title('Google Bard Chatbot')

#Initialising the session state variables
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

user_input=get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i],key="user"+str(i),is_user=True)



