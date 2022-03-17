import random 
print("Welcome to the number Guessing  Game")
print("I'm Thinking number between 1 to 100")
computer_number = random.randint(1,101)
print(computer_number)  
number=0
is_lives=False
def easy(lives):
    while lives>0:
        guess=int(input("Enter Guess a number \n"))
        if guess==computer_number:
            print("Congrants..You win")
            lives=0;
            break;
        elif(guess>computer_number):
            print("To high.... You go wrong")
            lives-=1
        else:
            print("To Low...You go wrong")
            lives-=1
    else:
        print("Game Over")
        is_lives=True 
# def hard():
#     lives=5
#     while lives>0:
#         guess=int(input("Enter Guess a number"))
#         if guess==computer_number:
#             print("Congrants..You win")
#             lives=0;
#             break;
#         elif(guess>computer_number):
#             print("To high.... You go wrong")
#             lives-=1
#         else:
#             print("To Low...You go wrong")
#             lives-=1
#     else:
#         print("Game Over")
#         is_lives=True     
def play_Game():
    while not is_lives:
        user_level=input("Choose a level easy or hard \n").lower()
        if user_level=="easy":
            lives=10
            easy(lives)
        elif(user_level=="hard"):
            lives=5
            easy(lives)
        else:
            print("You select wrong level")
while input("If you play this game press 'y' or 'n' to exit a game \n")=='y':
    is_lives=False
    play_Game()
else:
    is_lives=True
    print("okk.. You dont Play this Game")

        



