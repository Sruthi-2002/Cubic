import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

lss = sr.Recognizer()
eg = pyttsx3.init()
voices = eg.getProperty('voices')

eg.setProperty('voice', voices[1].id)

def talk(text):
    eg.say(text)
    eg.runAndWait()

eg.say('Hi I am your personal assistant, Cubic')
eg.say('What can I do for you?')
eg.runAndWait()


def take_command():
  try:
    with sr.Microphone() as source:
        print('listening...')
        voice = lss.listen(source)
        command = lss.recognize_google(voice)
        command = command.lower()
        if 'cubic' in command:
            command = command.replace('cubic', '')
            print(command)
  except:
    pass
  return command
def cubic():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
        print('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


cubic()
