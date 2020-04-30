import snowboydecoder
import sys
import signal
import speech_recognition as sr
import os
import pyttsx3
import requests

interrupted = False


def audioRecorderCallback(fname):
    print "converting audio to text"
    r = sr.Recognizer()
    with sr.AudioFile(fname) as source:
        audio = r.record(source)  # read the entire audio file
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print('input: ' + text)
        r = requests.get('http://api-robin.herokuapp.com/query/?phrase=' +
                         text)
        output = r.json()['response']
        print('output: ' + output)
        engine = pyttsx3.init()
        engine.say(output)
        engine.runAndWait()

    except sr.UnknownValueError:
        print "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from Google Speech Recognition service; {0}".format(
            e)

    os.remove(fname)


def detectedCallback():
    sys.stdout.write("recording audio...")
    sys.stdout.flush()


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


if len(sys.argv) == 1:
    print "Error: need to specify model name"
    print "Usage: python demo.py your.model"
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print "Listening... Press Ctrl+C to exit"

# main loop
detector.start(
    detected_callback=detectedCallback,
    audio_recorder_callback=audioRecorderCallback,
    interrupt_check=interrupt_callback,
    sleep_time=0.01)

detector.terminate()

