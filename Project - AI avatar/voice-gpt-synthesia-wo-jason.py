import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI
import time
import requests 
import json


# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI and Synthesia API key
OpenAI.api_key =os.getenv("OPENAI_API_KEY")
synthesia_api_key = os.getenv("SYNTHESIA_API_KEY")

# Initialize the recognizer
recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        # Adjust for ambient noise and record audio from the microphone
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        
        # Convert the audio to text
        user_input_text = recognizer.recognize_google(audio)
        user_input_text = user_input_text.lower()
        print(f"User said: {user_input_text}")

except KeyboardInterrupt:
    print('A KeyboardInterrupt encountered; Terminating the Program !!!')
    exit(0)
    
except sr.UnknownValueError:
    print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
    exit(1)

# Send the text to the OpenAI API
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input_text}
    ],
    max_tokens=25
)

# Print the response from the OpenAI API
print(response.choices[0].message)
gpt_response = response.choices[0].message

url = "https://api.synthesia.io/v2/videos"

payload = {
    "test": "true",
    "visibility": "private",
    "title": "MY 2ND VIDEO",
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
            "scriptText": "{gpt_response}",
            "avatar": "1706b274-9d21-4985-a558-35b3d6f704e4",
            "background": "green_screen"
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

