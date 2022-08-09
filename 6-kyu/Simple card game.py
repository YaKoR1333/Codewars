card_deck = "23456789TJQKA"


def winner(deck_steve: list[str], deck_josh: list[str]) -> str:
    steve_score = 0
    josh_score = 0
    for card_steve, card_josh in zip(deck_steve, deck_josh):
        if card_deck.index(card_steve) > card_deck.index(card_josh):
            steve_score += 1
        elif card_deck.index(card_steve) < card_deck.index(card_josh):
            josh_score += 1
    if steve_score > josh_score:
        return f'Steve wins {steve_score} to {josh_score}'
    elif steve_score < josh_score:
        return f'Josh wins {josh_score} to {steve_score}'
    else:
        return 'Tie'
