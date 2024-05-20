import streamlit as st
from langchain import PromptTemplate
from langchain_openai import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email

    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email:
    EMAIL: {email}
    
    RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["email"],
    template=template,
)
api_key = get_api_key()
client = OpenAI(api_key, base_url="https://api.aimlapi.com",) 
# def load_LLM(openai_api_key):
#     #llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)

st.set_page_config(page_title="Convert Text to Email")
st.markdown("## Enter Your Email To Convert")

def get_api_key():
    #input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    input_text = st.text_input(label="OpenAI API Key ",  type="password", key="openai_api_key_input")
    return input_text

def get_text():
    input_text = st.text_area(label="Type here", placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

def load_llm(input_text):    
    response = openai.Completion.create(  
        model="gpt-4",  
        messages=[  
    {  
    "role": "system", "content": "You are an Email Assitant.", 
     },  
    {  
    "role": "user", "content": input_text
    }  
    ],  
    )  
    message = response['choices'][0]['text']  
        
    return response


st.markdown("### Here is your Drafted Email:")
input_text = st.text_area(label="Type here", placeholder="Your Email...", key="email_input")
if email_input:
    if not openai_api_key:
        st.warning('Enter your OpenAI API Key.)', icon="🔥")
        st.stop()
    else
        prompt_with_email = prompt.format(email=email_input)
        formatted_email = load_llm(prompt_with_email)

st.write(formatted_email)



