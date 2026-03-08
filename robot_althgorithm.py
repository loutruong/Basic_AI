you=""
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
else:
    robot_brain = "I am fine thank you and you"

print("Robot:" + robot_brain)
