CARDS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

HANDS = {
    'High Card': [],
    'One Pair': [],
    'Two Pair': [],
    'Three of a Kind': [],
    'Full House': [],
    'Four of a Kind': [],
    'Five of a Kind': [],
}


def find_type_of_hand(hand_length, current_hand_data):
    type_of_hand = ''

    if hand_length == 1:
        type_of_hand = 'Five of a Kind'

    elif hand_length == 2:
        if 4 in current_hand_data.values():
            type_of_hand = 'Four of a Kind'
        elif 3 in current_hand_data.values():
            type_of_hand = 'Full House'

    elif hand_length == 3:
        if 3 in current_hand_data.values():
            type_of_hand = 'Three of a Kind'
        elif 2 in current_hand_data.values():
            type_of_hand = 'Two Pair'

    elif hand_length == 4:
        type_of_hand = 'One Pair'

    elif hand_length == 5:
        type_of_hand = 'High Card'

    return type_of_hand


with open('camel_cards_input.txt', 'r') as hands_list:
    for line in hands_list:
        hand, bid = line.strip().split()

        current_hand = {}

        for card in hand:
            if card not in current_hand:
                current_hand[card] = 0

            current_hand[card] += 1

        hand_type = find_type_of_hand(len(current_hand), current_hand)

        HANDS[hand_type].append((hand, bid))

total_winnings = 0
rank = 1


def sort_hand_data(hands):
    return sorted(hands, key=lambda hand_list: [CARDS[c] for c in hand_list[0]])


for hand_, hand_data in HANDS.items():
    current_hand_winnings = 0

    hand_data_sorted = sort_hand_data(hand_data)

    for h in hand_data_sorted:
        current_hand_winnings += int(h[-1]) * rank
        rank += 1

    total_winnings += current_hand_winnings

print(total_winnings)

