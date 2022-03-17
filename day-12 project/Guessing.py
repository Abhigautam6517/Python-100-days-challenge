from math import trunc
import random
print("Welcome to the number Guessing  Game")
print("I'm Thinking number between 1 to 100")
number=0

is_lives=False

computer_number = random.randint(1,101)
print(computer_number)
def play_game():
    while not is_lives:

        def easy(user):
            lives=4
            print("You have only 10 attempt to guessing a number")
            while lives>0:      
                guess_number=int(input("Guess a number"))
                if guess_number==computer_number:
                    print("You will Guess a number ")
                    print("congrants.....")
                    break;
                elif(guess_number>computer_number):   
                    print(f"Try again ..To high") 
                    
                else:
                    print("try again....To Low")
                    lives-=1
            else:   
                print("Game over")
                print(lives)
        user = input("Choose a level 'easy' or 'difficulity' ")
        easy(user)
    play_game()
while input(print("If you play Game Press 'y' or press 'n' To exit"))=='y':
    is_lives=False
    play_game()
    
else:
    is_lives=True
    print("Game exit")
        
        
        
    


