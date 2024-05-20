import os
import openai
from openai import OpenAI
import streamlit as st
from langchain import PromptTemplate

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

api_key="c45e8e03e070469bbea48b070fd8eaf1" 



st.set_page_config(page_title="Convert Text to Email")
st.markdown("## Enter Your Email To Convert")
input_text = st.text_area(label="Type here", placeholder="Your Email...", key="email_input")

prompt_with_email = prompt.format(email=input_text)

## Define 
client = OpenAI(
api_key,
base_url="https://api.aimlapi.com",
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "system",
        "content": "You are an Email assistant who knows everything.",
    },
              {
                  "role": "user",
                  "content": prompt_with_email
              }
             ],
)

message =response.choices[0].message.content
st.write(message)
# print(f"Assistant: {message}")
