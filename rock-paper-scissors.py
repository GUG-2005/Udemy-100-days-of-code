rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]

user = int(input("What is your pick? Type 0 for Rock, 1 for Paper and 2 for Scissors!\n"))

for i in range(len(rps)):
    if user == i:
        print(rps[i])

random_n = random.randint(0, len(rps) -1)

for j in range(len(rps)):
    if random_n == j:
        print("Computer Chose")
        print(rps[random_n])

if i > random_n:
    print("You Win")
elif i == random_n:
    print("The match is draw!")
else:
    print("You Lose")
