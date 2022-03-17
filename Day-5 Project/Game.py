import random

Toss = ["head", "tail","head", "tail","head", "tail","head", "tail","head", "tail","head", "tail",]
user = input("What you choose \n").lower()
computer_choice = random.choice(Toss)
print(f"You choose a {user}")
print("computer choose a" +" " +computer_choice)
if user =="head" or user=="tail":
    if user==computer_choice:
        print("Match Won")
    else:
     print("Match Loose")
else:
    print("you choose invalid command")