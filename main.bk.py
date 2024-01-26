from card import Deck
from player import Player


# While the Player is hitting yes to play, the loop will continue. yes = True,no = False
def player_wants_to_hit():
    user_input = input("Do you want to hit? (yes/no): ").lower()
    # print("User input:", user_input) # Add this line for debugging
    return user_input == 'y'


def dealer_should_hit(dealer_hand_value):
    # Example: Dealer hits if the hand value is less than 17
    return dealer_hand_value < 17


def show_game_info(player, dealer, gstate):
    print("-------------------")
    print("Player Hand:")
    player.show_hand()
    print(f"Hand Value: {player.hand_value()}")
    print("-------------------")
    print("Dealer Hand:")
    dealer.show_hand_dealer(gstate)
    print("-------------------")


def main():
    player = Player("Player 1")
    dealer = Player("Dealer")

    state = True

    # Deal initial cards
    for i in range(2):
        player.join_card(deck.deal_card())
        dealer.join_card(deck.deal_card())

    # Game loop
    while state:
        show_game_info(player, dealer, state)

        # Player's turn
        while player_wants_to_hit():
            player.join_card(deck.deal_card())
            player.show_hand()
            print(player.hand_value())

            # Check for bust or blackjack
            if player.hand_value() > 21:
                state = False
                break
            elif player.hand_value() == 21:
                state = False
                break

        # Dealer's turn
        while dealer_should_hit(dealer.hand_value()):
            dealer.join_card(deck.deal_card())
            # Check for bust or blackjack
            if dealer.hand_value() > 21:
                state = False
            elif dealer.hand_value() == 21:
                state = False
        else:
            break

    state = False
# Determine winner and display result
    if player.hand_value() > 21:
        print("Dealer Won")
    elif dealer.hand_value() > 21:
        print("Player Won!!")
    elif player.hand_value() > dealer.hand_value():
        print("Player Won!!")
    elif dealer.hand_value() > player.hand_value():
        print("Dealer Won")
    else:
        print("Empate.")
    show_game_info(player, dealer, state)

# Ask if the player wants to play again


# Initialize deck and players
deck = Deck()
deck.shuffle()

main()

# Calcular a vitória com base no valor não funciona pois quem rebenta tem sempre mais do que quem ganha.
# Responder 'no' não funciona para sair do loop. Verificar razão.
