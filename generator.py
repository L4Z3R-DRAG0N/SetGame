import random
def gen_set():
    shape = ("O", "S", "D")
    fill = ("E", "L", "F")
    color = ("R", "P", "G")
    number = (1, 2, 3)

    card_set = []

    while (len(card_set) < 12):
        new_card = [
            random.choice(shape),
            random.choice(fill),
            random.choice(color),
            random.choice(number)
            ]
        
        if not new_card in card_set:
            card_set.append(new_card)

    return card_set