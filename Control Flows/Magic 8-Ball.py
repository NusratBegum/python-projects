"""
1.In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.

2.Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.

3.We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.

4.Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

5. finally, we’ll use a control flow to programmatically give an answer to the question we asked the Magic 8-Ball. Declare a conditional statement that checks if the random_number is equal to 1. If so, answer should be set to the phrase "Yes - definitely.".

"""

import random
name = "Nusrat"
question = "Will I win the match?"
answer = ""
random_number = random.randint(1, 9)
#print(random_number)
 
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer= "Ask again later."
elif random_number == 6:
  answer="Better not tell you now."
elif random_number == 7:
  answer="My sources say no."
elif random_number == 8:
  answer="Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"
print(" asks: " + question)
print("Magic 8 Ball's answer: " + answer)







