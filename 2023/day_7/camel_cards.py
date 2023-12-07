from collections import Counter


def jokerize(hand):
    target = (c := Counter(hand)).most_common()[0][0]
    if target == "J" and hand != "JJJJJ":
        target = c.most_common()[1][0]
    return hand.replace("J", target)


def score(hand, joker=False):
    tiebreaker = ["23456789TJQKA".index(c) for c in hand]
    if joker:
        tiebreaker = ["J23456789TQKA".index(c) for c in hand]
        hand = jokerize(hand)
    match sorted(Counter(hand).values()):
        case [5]: points = 6
        case [1, 4]: points = 5
        case [2, 3]: points = 4
        case [1, 1, 3]: points = 3
        case [1, 2, 2]: points = 2
        case [1, 1, 1, 2]: points = 1
        case _: points = 0
    return points, tiebreaker


def total_winnings(ccs, joker=False):
    ccs = sorted(ccs, key=lambda cc: score(cc[0], joker=joker))
    return sum(int(bet) * i for i, (_, bet) in enumerate(ccs, 1))


if __name__ == "__main__":
    with open("input.txt") as file:
        camel_cards = [line.split() for line in file.read().splitlines()]

    print(total_winnings(camel_cards))
    print(total_winnings(camel_cards, joker=True))
