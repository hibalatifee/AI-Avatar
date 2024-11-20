import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI
import time
import requests 
import json
import  streamlit as st


# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI and Synthesia API key
OpenAI.api_key =os.getenv("OPENAI_API_KEY")
synthesia_api_key = os.getenv("SYNTHESIA_API_KEY")

st.title("The Next School AI Avatar")
st.subheader("Hello! Welcome to the AI Avatar :wave:")
st.write('Ask anything')
    

# Initialize the recognizer
recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        # Adjust for ambient noise and record audio from the microphone
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        #print("Listening...")
        st.write('Barry is listening...')
        audio = recognizer.listen(source, timeout=10)
        
        # Convert the audio to text
        user_input_text = recognizer.recognize_google(audio)
        user_input_text = user_input_text.lower()
        print(f"User said: {user_input_text}")
        #st. write('User said: {user_input_text}')

except KeyboardInterrupt:
    print('A KeyboardInterrupt encountered; Terminating the Program !!!')
    exit(0)
    
except sr.UnknownValueError:
    #print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
    st.write('Can you say it again?')
    exit(1)

# Send the text to the OpenAI API
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input_text}
    ],
    max_tokens=500
)

# Print the response from the OpenAI API
print(response.choices[0].message)

with st.spinner('Wait for it...'):
    gpt_response = response.choices[0].message.content


    url = "https://api.synthesia.io/v2/videos"

    payload = {
        "test": "true",
        "visibility": "private",
        "title": "Barry says",
        "input": [
            {
                "avatarSettings": {
                    "horizontalAlign": "center",
                    "scale": 1,
                    "style": "rectangular",
                    "seamless": False
                },
                "backgroundSettings": { "videoSettings": {
                        "shortBackgroundContentMatchMode": "freeze",
                        "longBackgroundContentMatchMode": "trim"
                    } },
                "scriptText": gpt_response,
                "avatar": "5f962c13-4c8e-4f81-a8dd-736b42403144",
                "background": "open_office"
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "a3a7f20e6e8aa1fd72d299c4f2559e7a"
    }


    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    time.sleep(60)

st.write('Barry is ready')


