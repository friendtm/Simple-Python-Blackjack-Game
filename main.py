from card import Deck
from player import Player


def player_wants_to_hit():
    return input("Do you want to hit? (yes/no): ").lower() == 'y'


def dealer_should_hit(dealer_hand_value):
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


def determine_winner(player, dealer):
    if player.hand_value() > 21:
        return "Dealer"
    elif dealer.hand_value() > 21:
        return "Player"
    elif player.hand_value() > dealer.hand_value():
        return "Player"
    elif dealer.hand_value() > player.hand_value():
        return "Dealer"
    else:
        return "Tie"


def determine_bj(player, dealer):
    if player.hand_value() == 21:
        print("Player Blackjack!!")
        state = False
    elif dealer.hand_value() == 21:
        print("Dealer Blackjack.")
        state = False
    else:
        state = True
    return state


def play_game():
    player = Player("Player 1")
    dealer = Player("Dealer")

    # Deal initial cards
    for _ in range(2):
        player.join_card(deck.deal_card())
        dealer.join_card(deck.deal_card())

    # Game loop
    state = determine_bj(player, dealer)

    while state:
        show_game_info(player, dealer, state)

        # Player's turn
        while player_wants_to_hit():
            player.join_card(deck.deal_card())
            player.show_hand()
            if player.hand_value() > 21:
                state = False
                break
            elif player.hand_value() == 21:
                state = False
                break

        # Dealer's turn
        while dealer_should_hit(dealer.hand_value()):
            dealer.join_card(deck.deal_card())
            if dealer.hand_value() > 21 or dealer.hand_value() == 21:
                state = False
                break
        else:
            break
    state = False
    # Determine winner and display result
    winner = determine_winner(player, dealer)
    print(f"{winner} won!")
    show_game_info(player, dealer, state)


# Initialize deck and players
deck = Deck()
deck.shuffle()

# Play the game
play_game()
