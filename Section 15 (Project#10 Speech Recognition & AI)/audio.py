import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander


def say():
    subprocess.call('ptts -u "k.txt"', shell=True)

# playing any wave file
def play_audio(filename):
    chunk = 1024  # chunk size
    wf = wave.open(filename, 'rb')  # opening the file as binary wave file, read mode
    pa = pyaudio.PyAudio()  # instantiating the PyAudio Class

    # creating a stream/sound, loading the file into some binary object
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    # new data stream variable from the original chunk
    data_stream = wf.readframes(chunk)

    # while there is more stream to read, we are writing the audio stream to our stream
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


# setting up the recognizer, it will recognize when I will talk to the microphone
r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening..")
    play_audio('audio/sound.wav')  # starting notification sound

    # Listening from microphone
    with sr.Microphone() as source:
        print("Say something..")
        audio = r.listen(source)  # capturing the audio

    play_audio("./audio/sound.wav")  # ending notification sound

    command = ""

    try:
        command = r.recognize_google(audio)  # using google to do speech-to-text
        print(command)
        print("wait... responding")
    except:
        command = "Couldn't understand you"

    if command in cmd.exit:
        global Running
        Running = False
        cmd.respond("Okay. Bye for now. Talk to you soon!")
    elif command is "Couldn't understand you":
        cmd.respond("Couldn't understand you")
    else:
        cmd.discover(command)

Running = True

while Running is True:
    initSpeech()
