import News_api
user_input = input("What news do you want to see?: , enter q for Quit").lower()

while True:
    if (user_input == "q"):
        quit()
    elif (user_input == "Weather"):
