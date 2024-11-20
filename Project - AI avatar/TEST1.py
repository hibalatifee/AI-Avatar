import wave
import sys
import speech_recognition as sr
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5

with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

    print('Recording...')
    for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
        wf.writeframes(stream.read(CHUNK))
    print('Done')

   # stream.close()
   # p.terminate()

# initialize the recognizer
r = sr.Recognizer()

#with sr.AudioFile('output.wav') as source:
with sr.AudioSource('output.wav') as source:
    # listen for the data (load audio to memory)
    audio_data = r.listen(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
    