import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

list = ["My","Name","Is","Hari"]

for i in list:
    print("Shoutout to"+i)

for name in list:
    names = name.split()
    shoutout = f' {names[0]}'
    speaker.Speak(shoutout)
