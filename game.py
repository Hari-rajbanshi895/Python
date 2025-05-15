import os
import time
import pyttsx3
import ctypes

REPEAT_INTERVAL = 3600  # repeat frequency in seconds

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

while True:
    # Speaking the message
    engine.say("Hari is a good boy")
    engine.runAndWait()

    # Displaying a message box
    ctypes.windll.user32.MessageBoxW(0, "hari", "Alert", 0x100 | 0x1)

    # Wait before repeating
    time.sleep(REPEAT_INTERVAL)
