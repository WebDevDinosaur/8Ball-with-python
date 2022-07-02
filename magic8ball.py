import random

name = "Leroy"
question = "Will I be famous?"
#question = ""
answer = ""

#print(random_number)
random_number = random.randint(1, 10)

#if / elif statements
if random_number == 1:
  answer = "Yes - definitely!"
elif random_number == 2:
  answer = "It is decidely so!"
elif random_number == 3:
  answer = "Without a doubt!"
elif random_number == 4:
  answer = "Reply hazy, try again!"
elif random_number == 5:
  answer = "Ask again later!"
elif random_number == 6:
  answer = "Better not tell you now!"
elif random_number == 7:
  answer = "My sources say no!"
elif random_number == 8:
  answer = "Outlook not so good!"
elif random_number == 9:
  answer = "Very doubtful!"
elif random_number == 10:
  answer = "Not on you nelly!"
else: answer == "Error!!"

#conditions to be met

if name and question: 
  print(name + " wants to know: " + question)
elif name == "" and question:
  print("Question: " + question)

if question:
  print("Magic 8-Ball's answer: " + answer)
elif name and question == "":
  print(name + " please ask a question!")
else:
  print("Please ask a question!")
