# Import Section
import pyttsx3
import speech_recognition
from datetime import date, datetime

# Variable Init
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
robot_mouth = pyttsx3.init()

while True:
    # Robot Listening
    with speech_recognition.Microphone() as mic:
        print("Robot: I am listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You:" + you)

    # Robot Algorithm
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Lou"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H:%M:%S")
    elif "president" in you:
        robot_brain = "Donald trump"
    elif "bye" in you:
        robot_brain = "Bye Lou"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I am fine thank you and you"

    print("Robot:" + robot_brain)

    # Robot Speech
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
