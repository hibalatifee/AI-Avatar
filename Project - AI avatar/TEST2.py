import wave
import sys
import speech_recognition as sr
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILE = 'output.wav'

# Recording audio
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print('Recording...')
frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print('Done recording')

# Stop and close the stream 
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a file
with wave.open(OUTPUT_FILE, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# Recognizing the audio file using SpeechRecognition
r = sr.Recognizer()

with sr.AudioFile(OUTPUT_FILE) as source:
    audio_data = r.record(source)  # read the entire audio file
    try:
        text = r.recognize_google(audio_data)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
