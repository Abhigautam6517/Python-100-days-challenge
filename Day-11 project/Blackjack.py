import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = random.choice(cards)
    return user

def calc_score(cards):
    if sum(cards)==21 and len(cards):
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(21)  
    return sum(cards)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        print("you loose")
    if user_score==computer_score:
        print("match draw")
    elif(user_score==0):
        print("You loose")
    elif(computer_score==0):
        print("Win with a blackjack")
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif(user_score>computer_score):
        print("You win")
    else:
        print("you loose")

 
def play_game()

    user_cards=[]
    deal_cards=[]
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        deal_cards.append(deal_card())
        while not is_game_over:
            user_score=calc_score(user_cards)
            computer_score=calc_score(deal_cards)
            print(f"   Your cards: {user_cards}, current score: {user_score}")
            print(f" Computer's first card: {deal_cards[0]}")
            

            if user_score == 0 or computer_score == 0 or user_score > 21:
                 is_game_over = True
            else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            deal_cards.append(deal_card())
            computer_score = calc_score(deal_cards)
        

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {deal_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":


    play_game()




    # print(user_cards)
    # print(deal_cards)

