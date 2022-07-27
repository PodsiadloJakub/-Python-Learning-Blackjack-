from art import logo
import random

print(logo)
player = {
    "Money": 100,
    "CardsValue": 0,
}
player_hand = []

opponent = {
    "Money": 100,
    "CardsValue": 0,
}
opponent_hand = []

hearts = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
spades = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
diamonds = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
clubs = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

turn = ""

actions = ["Draw <", "Pass <", "Cheat <"]


def Gameplay(turn):
    for a in actions:
        print(a)
        print("")
    while turn == "player":
        action = input("What do you want do? Choose one option: ")
        if action == "Draw":
            Draw("player")
        else:
            turn = "opponent"
            print("Opponent's turn!")
            opponentAI()


def Draw(player_name):
    if player_name == "player":
        value = random.randrange(1, 5)
        HandingOutCardsForPlayer(CardSymbol(value))
    elif player_name == "opponent":
        value = random.randrange(1, 5)
        HandingOutCardsForOpponent(CardSymbol(value))
        opponentAI()


def HandingOutCardsForPlayer(symbol):
    print(symbol)
  #ustawiam na sztywno hearts bo nie chce mi sie teraz rozkminiać
    selected_card = random.choice(hearts)
    print(selected_card)
    player_hand.append(selected_card)
    player["CardsValue"] += selected_card
    print(player)


def HandingOutCardsForOpponent(symbol):
    print(symbol)
  #ustawiam na sztywno hearts bo nie chce mi sie teraz rozkminiać
    selected_card = random.choice(hearts)
    print(selected_card)
    opponent["CardsValue"] += selected_card
    print(opponent)


def CardSymbol(value):
    switcher = {
        1: "hearts",
        2: "spades",
        3: "diamonds",
        4: "clubs",
    }
    return switcher.get(value, "")


def opponentAI():
    opponent_hand_value = opponent["CardsValue"]
    x = random.randint(14, 18)
    if opponent_hand_value <= x:
        Draw("opponent")


Gameplay("player")
