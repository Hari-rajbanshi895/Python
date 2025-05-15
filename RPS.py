# Rock paper Scissor program
import random
comp = random.randint(0,2)
user = int(input("Enter 0 for rock, 1 for paper and 2 for sicssor:\n"))

def check(comp,user):
    if (comp == user):
        return 0
    if (comp == 0 and user == 2):
        return -1
    if (comp == 1 and user == 0):
        return -1
    if (comp == 2 and user == 1):
        return -1
    return 1

score = check(user,comp)
if (score == 0):
    print("Its Draw")
elif (score == -1):
    print("You Lose")
elif (score == 1):
    print("You Won")

print("Player: ",user)
print("Computer: ",comp)

        

    







