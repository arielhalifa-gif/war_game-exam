import ..utils.deck
def create_player(name:str) -> dict:
    player_dict = {}
    player_dict["name"] = name
    player_dict["hand"] = []
    player_dict["won_pile"] = []
    return player_dict



def init_game()->dict:
    player1 = create_player("moshe")
    try:
        player2 = create_player()
    except TypeError:
        player2 = create_player("AI")
    new_deck = deck.create_deck()
    shuffled_deck = deck.shuffle(new_deck)
    player1["hand"] = shuffled_deck[:26]
    player1["hand"] = shuffled_deck[26:]
    return {
        "deck": shuffled_deck,
        "player1": player1,
        "player2": player2
        }



def play_round(player_1: dict, player_2: dict)-> None:
    top_card1 = player_1["hand"].pop()
    top_card2 = player_2["hand"].pop()
    winner = compare_cards(top_card1, top_card2)
    if winner == "p1":
        player_1["won_pile"].append(top_card1)
        player_1["won_pile"].append(top_card2)
        print("player 1 has won this round")
    elif winner = "p2":
        player_2["won_pile"].append(top_card1)
        player_2["won_pile"].append(top_card2)
        print("player 2 has won this round")
    else:
        print(f"{winner} nothing to do for now")