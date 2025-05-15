""" Create a program capable of displaying questions to the user """

question = 'What is the capital of Nepal'
print(question)
options = ["kathmandu","lalitpur","jhapa","bhaktapur"]
answer = input('Enter the answer: ')

if answer in options == "kathmandu":
    print("Correct ans")
else:
    print("Wrong answer")

# def answer1(answer,option2):
#     if answer == option2:
#         print('Correct answer')
#         print('You won 1$')
#     else: 
#         print('Wrong answer!')

# answer1(answer,option2)

# question = ['What is the capital of Nepal']
# print(question)
# options = ['Bhaktapur','Jhapa','Kathmandu','Lalitpur']
# print(options)
# change = tuple(options)

# answer = input('Enter the answer: ')

# def price(change,answer):
#     if answer in change == 'kathmandu':
#         print('Correct answer')
#         print('Congrats you  have won 1$')
#     else:
#         print('Wrong answer!')

# price(options,answer)

