from os import system
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card"""
    randm_card = random.choice(cards)
    return randm_card


 
def calculate_score(list_of_cards):
    """Calculates score for a player"""
    
    
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
            
    return sum(list_of_cards)

#print(user_cards)
#print(computer_cards)
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


        
def play_game():
    user_cards = []
    computer_cards = []
    game_ends = False
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_ends:
        comp = calculate_score(computer_cards)
        usr = calculate_score(user_cards)   

        print(f"Your cards are {user_cards}, current score is: {usr}")
        print(f"Computer's first card is {computer_cards[0]}")
                

        if comp == 0 or usr == 0 or usr > 21:
            #print("Game over")
            game_ends = True
        else:
            deal = input("Do you want to add another card?")
            if deal == "y":
                user_cards.append(deal_card())
            else:
                game_ends = True  
    
    while comp != 0 and comp < 17:
        computer_cards.append(deal_card())
        comp = calculate_score(computer_cards)

        print(f"   Your final hand: {user_cards}, final score: {usr}")
        print(f"   Computer's final hand: {computer_cards}, final score: {comp}")
        print(compare(usr, comp))
        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    system("cls")
    play_game()