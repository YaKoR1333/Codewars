def mirror(text: str) -> str:
    mirror_message = ''
    max_len_string = len(max(text.split()))
    for word in text.split():
        mirror_message += f'* {word[::-1]}' + ' ' * (max_len_string - len(word)) + ' *\n'
    return '*' * (max_len_string + 4) + '\n' + mirror_message + '*' * (max_len_string + 4)
