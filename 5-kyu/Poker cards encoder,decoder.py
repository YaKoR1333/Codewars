def get_number_dict() -> dict:
    return {
        'A': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
    }


def get_suit_dict() -> dict:
    return {
        'c': 0,
        'd': 1,
        'h': 2,
        's': 3,
    }


def encode(cards: list) -> list:
    encode_number_dict = get_number_dict()
    encode_suit_dict = get_suit_dict()
    return sorted(list(map(lambda x: encode_number_dict.get(x[0]) + encode_suit_dict.get(x[1]) * 13, cards)))


def decode(cards: list) -> list:
    decode_number_dict = {v: k for k, v in get_number_dict().items()}
    decode_suit_dict = {v: k for k, v in get_suit_dict().items()}
    return list(map(lambda x: decode_number_dict.get(x % 13) + decode_suit_dict.get(x // 13), sorted(cards)))
