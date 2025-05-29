# game about blackjack
import random
# Cards

class DECK:
    @staticmethod
    def card_deal():
        suits = ["♠", "♥", "♦", "♣"]
        faces = ["A", "K", "Q", "J"] + list(range(2, 11))
        return random.choice(suits), random.choice(faces)
    



# cash systems
scash = 100

# Saving cash system
# Reset Cash systems
# Cash input

def game_start():   


    gamblecash = int(input(f"Enter cash! You have {scash} cash: "))
    suit, face = DECK.card_deal()
    suit2, face2 = DECK.card_deal()
    dealer_suit1, dealer_face1 = DECK.card_deal()
    dealer_suit2, dealer_face2 = DECK.card_deal()
    def get_card_value(face, current_total=0):
        if face == "A":
            # If adding 11 keeps us <= 21, use 11, else use 1
            return 11 if current_total + 11 <= 21 else 1
        elif face in ["K", "Q", "J"]:
            return 10
        else:
            pass
            return int(face)
        
    print(f"Your cards: {suit} {face}, {suit2} {face2}")
    userinputs = input("Would you like to hit or stand? (h/s) ")
    # Check if the player wants to hit or stand 
    total_value = face + face2
    if userinputs.lower() == 'h':
        # Player chooses to hit
        new_suit, new_face = DECK.card_deal()
        print(f"You drew {new_suit} {new_face}.")
        # Update the player's hand value
        new_value = get_card_value(new_face)
        total_value += new_value
        print(f"Your total value is now {total_value}.")
    elif userinputs.lower() == 's':
        # Player chooses to stand
        print("You chose to stand.")
    dealer_value1 = get_card_value(dealer_face1)
    dealer_value2 = get_card_value(dealer_face2)
    total_dealer = dealer_value1 + dealer_value2
    newdealersuit = None

    while total_dealer <= 16:
        newdealersui, newdealerface = DECK.card_deal()
        print(f"Dealer hits and gets {newdealersuit} {newdealersuit}.")
        dealer_value3 = get_card_value(newdealersuit)
        total_dealer += dealer_value3

    if total_dealer > 21:
        print("Dealer busts! You win!")
        dealerbust = True
        scash += gamblecash

    elif total_dealer == total_value:
        print("It's a tie!")
        dealerbust = False

    elif total_value > 21:
        print("You bust! Dealer wins!")
        scash -= gamblecash

    elif total_value > total_dealer:
        print("You win!")
        scash += gamblecash

    else:
        print("Dealer wins!")
        scash -= gamblecash
    print(f"Your current cash is {scash}.")

    gamerequest = input("Would you like to play again? (y/n) ")
    if gamerequest.lower() == 'y':
        game_start()
    else:
        print("Thanks for playing!")
        pass


game_start()