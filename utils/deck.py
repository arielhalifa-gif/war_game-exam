import random
def  create_card(rank:str, suite:str) -> dict:
    card_dict = {}
    card_dict["rank"] = rank
    card_dict["suite"] = suite
    if rank.isdigit():
        card_dict["value"] = int(rank)
    elif rank == "J":
        card_dict["value"] = 11
    elif rank == "Q":
        card_dict["value"] = 12
    elif rank == "K":
        card_dict["value"] = 13
    elif rank == "A":
        card_dict["value"] = 14
    return card_dict


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else: # p1 = p2
        return "WAR"


def create_deck() -> list[dict]:
    complete_deck = []
    lst_values = ["H", "C", "D", "S"]
    lst_big_cards = ["J", "Q", "K", "A"]
    for val in lst_values:
        for i in range(2,11):
            complete_deck.append(create_card(str(i), val))
        for type in lst_big_cards:
            complete_deck.append(create_card(str(i), val))
    return complete_deck


def shuffle(deck: list[dict]) -> list[dict]:
    for i in range(1000):
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        while index1 == index2:
            index1 = random.randint(0, 51)
            index2 = random.randint(0, 51)
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck
