from itertools import cycle


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encode_text = ''
        if (text[1] == text[1].upper()) and (ord(text[1].upper()) != ord(text[1].lower())):
            return text
        else:
            for idx, ch in enumerate(zip(text, cycle(self.key))):
                if self.alphabet.count(ch[0]) == 0:
                    encode_text += ch[0]
                else:
                    encode_text += self.alphabet[(self.alphabet.index(ch[0]) + self.alphabet.index(ch[1])) %
                                                 len(self.alphabet)]
        return encode_text

    def decode(self, text):
        decode_text = ''
        if (text[1] == text[1].upper()) and (ord(text[1].upper()) != ord(text[1].lower())):
            return text
        else:
            for idx, ch in enumerate(zip(text, cycle(self.key))):
                if self.alphabet.count(ch[0]) == 0:
                    decode_text += ch[0]
                else:
                    decode_text += self.alphabet[(self.alphabet.index(ch[0]) - self.alphabet.index(ch[1])) %
                                                 len(self.alphabet) % len(self.alphabet)]
        return decode_text
