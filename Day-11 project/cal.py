import random

is_game=False
dice = [1,2,3,4,5,6]

def computer_dice(value,computer_value):
    while not is_game:
        if value<7:
            if(value>computer_value):
                print("you win")
                break;
            else:
                print("You loose")
                break;
        else:
            print("You type a invalid number")
            break;
   


while input("you contiue this game type 'Y' or Exit this game type 'n'")=="y":
        is_game=False
        value = int(input(f"Type your dice {1,2,3,4,5,6,} \n"))
        computer_value=random.choice(dice)
        computer_dice(value,computer_value)
else:
    is_game=True
    print("exit")



    


    
