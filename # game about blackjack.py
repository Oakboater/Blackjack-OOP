# Rewrote the entire Blackjack code to clean up and work on
import random 
class DECK:  
    def __init__(self):  
        self.reset()

    def reset(self):  
        self.suit = ["♥", "♠", "♦", "♣"]  
        self.face = ["K", "Q", "J", "A"] + [str(n) for n in range(2, 11)]  
        self.cards = [f"{f}{s}" for s in self.suit for f in self.face]  
        random.shuffle(self.cards)  

    def draw_card(self):  
        if not self.cards:  
            self.reset()  
            print("\n--- DECK RESHUFFLED ---")  
        return self.cards.pop()  


deck = DECK()

class Cash:
    def __init__(self, amount):
        self.amount = amount

    def win(self, value):
        self.amount += value

    def lose(self, value):
        self.amount -= value

    def get_balance(self):
        return self.amount
     

    
player_cash = Cash(100)
print("Welcome to BlackJack.")

def gamestart():
    while True:
        try:
            cash_input = int(input(f"How much would you like to bet? You have {player_cash.get_balance()}: "))
            if 0 < cash_input <= player_cash.get_balance():
                break
            else:
                print(f"Please enter a valid amount up to your balance ({player_cash.get_balance()}).")
        except ValueError:
            print("Please enter a valid number.")
    card1 = deck.draw_card()
    card2 = deck.draw_card()
    print(f"Your starting cards are: {card1}, {card2}")
    return [card1, card2], cash_input

def dealer():
    dcard1 = deck.draw_card()
    dcard2 = deck.draw_card()
    print(f"Dealer reveals a card, its {dcard1}")
    return dcard1, dcard2


def userinputs(current_cards):
    while True:
        try:
            user_input = input("Would you like to (H)it or (S)tand? ").lower()
            if user_input == "h":
                new_card = deck.draw_card()
                current_cards.append(new_card)
                print(f"You have picked up a {new_card}. Your current cards are: {', '.join(current_cards)}")
            elif user_input == "s":
                print(f"You decided to stand with: {', '.join(current_cards)}")
                break
            else:
                print("You have not selected a valid response")
                userinputs(current_cards)
        except Exception as e:
            print("An error occurred:", e)
            return current_cards
def card_value(card):
    face = card[:-1]
    if face in ['K', 'Q', 'J']:
        return 10
    elif face == 'A':
        return 11
    else:
        return int(face)

def hand_value(cards):
    value = sum(card_value(card) for card in cards)
    # Adjust for Aces
    aces = sum(1 for card in cards if card[:-1] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def dealerhits(dealer_cards):
    # Dealer hits until reaching 17 or more
    while hand_value(dealer_cards) < 17:
        new_card = deck.draw_card()
        dealer_cards.append(new_card)
        print(f"Dealer draws a card: {new_card}. Dealer's cards: {', '.join(dealer_cards)}")
    print(f"Dealer stands with: {', '.join(dealer_cards)} (Value: {hand_value(dealer_cards)})")
    return dealer_cards

while True:
    (player_cards, bet) = gamestart()
    dcard1, dcard2 = dealer()
    dealer_cards = [dcard1, dcard2]

    # Check for player blackjack
    player_blackjack = hand_value(player_cards) == 21 and len(player_cards) == 2
    dealer_blackjack = hand_value(dealer_cards) == 21 and len(dealer_cards) == 2

    if player_blackjack and dealer_blackjack:
        print(f"Both you and the dealer have blackjack! It's a tie.")
        print(f"Your hand: {', '.join(player_cards)} (Value: 21)")
        print(f"Dealer's hand: {', '.join(dealer_cards)} (Value: 21)")
    elif player_blackjack:
        print(f"Blackjack! You win 1.5x your bet!")
        print(f"Your hand: {', '.join(player_cards)} (Value: 21)")
        player_cash.win(int(1.5 * bet))
    elif dealer_blackjack:
        print(f"Dealer has blackjack! Dealer wins.")
        print(f"Dealer's hand: {', '.join(dealer_cards)} (Value: 21)")
        player_cash.lose(bet)
    else:
        userinputs(player_cards)
        player_total = hand_value(player_cards)
        dealerhits(dealer_cards)
        dealer_total = hand_value(dealer_cards)

        print(f"Your hand: {', '.join(player_cards)} (Value: {player_total})")
        print(f"Dealer's hand: {', '.join(dealer_cards)} (Value: {dealer_total})")

        if player_total > 21:
            print("You busted! Dealer wins.")
            player_cash.lose(bet)
        elif dealer_total > 21 or player_total > dealer_total:
            print("You win!")
            player_cash.win(bet)
        elif player_total < dealer_total:
            print("Dealer wins!")
            player_cash.lose(bet)
        else:
            print("It's a tie!")

    print(f"Your balance: {player_cash.get_balance()}")
    if player_cash.get_balance() <= 0:
        print("You are out of money! Game over.")
        break

    play_again = input("Play another round? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
