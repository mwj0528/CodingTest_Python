def solution(s):
    words = s.split(' ')
    result = []

    for word in words:
        if word == "":
            result.append("")
            continue
        new_word = ''
        for i, ch in enumerate(word):
            if ch.isdigit():
                new_word += ch
            elif i == 0:
                new_word += ch.upper()
            else:
                new_word += ch.lower()
        result.append(new_word)

    return ' '.join(result)
