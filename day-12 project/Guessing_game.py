from math import trunc
import random

number=0

is_lives=False

computer_number = random.randint(1,101)
# print(computer_number)
def play_game(user):
    print("Welcome to the number Guessing  Game")
    print("I'm Thinking number between 1 to 100")
    while not is_lives:
        if user=="easy":
            lives=4
            print("You have only 10 attempt to guessing a number")
            while lives>0:      
                guess_number=int(input("Guess a number"))
                if guess_number==computer_number:
                    print("You will Guess a number ")
                    print("congrants.....")
                    
                elif(guess_number>computer_number):   
                    print(f"Try again ..To high") 
                    
                else:
                    print("try again....To Low")
                    lives-=1
            # else:   
            #     print("Game over")
            #     print(lives)
        elif user=="difficult":
            lives=5
            print("You have only 5 attempt to guessing a number")
            while lives>1:      
                guess_number=int(input("Guess a number"))
                if guess_number==computer_number:
                    print("You will Guess a number ")
                    print("congrants.....")
                    lives=0
                elif(guess_number>computer_number):   
                    print(f"Try again ..To high") 
                    
                else:
                    print("try again....To Low")
                    lives-=1
            else:   
                print("Game over")
                print(lives)
        else:
            print("Please select Valid Level")
    else:
        print("Game exit")
            
    
while input(print("If you play Game Press 'y' or press 'n' To exit \n"))=='y':
    is_lives=False
    user = input("Choose a level 'easy' or 'difficult' ")
    play_game(user)
    
# else:
#     is_lives=True
#     print("Game exit")
        
        
        
    


