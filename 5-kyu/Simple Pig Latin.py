def pig_it(text: str) -> str:
    new_text = ''
    for word in text.split():
        if word in '!?.,&':
            new_text += word
        else:
            new_word = word[1:] + word[0] + 'ay'
            new_text += new_word + ' '
    return new_text.strip()
