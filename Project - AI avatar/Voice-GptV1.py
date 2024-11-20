import speech_recognition
from dotenv import load_dotenv
import os
from openai import OpenAI
import time
load_dotenv()
OpenAI.api_key =os.getenv("OPENAI_API_KEY")
flag = 1


# The Recognizer is initialized.
UserVoiceRecognizer = speech_recognition.Recognizer()
 
#while(1):
try:
    with speech_recognition.Microphone() as UserVoiceInputSource:
 
        UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
 
        # The Program listens to the user voice input.
        UserVoiceInput = UserVoiceRecognizer.listen(source=UserVoiceInputSource, timeout=10)
 
        UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
        UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
        print(UserVoiceInput_converted_to_Text)
    
except KeyboardInterrupt:
        print('A KeyboardInterrupt encountered; Terminating the Program !!!')
        exit(0)
    
except speech_recognition.UnknownValueError:
        print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")


client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": UserVoiceInput_converted_to_Text}
    ])

print(completion.choices[0].message)
