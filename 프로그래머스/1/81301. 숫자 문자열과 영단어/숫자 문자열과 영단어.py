def solution(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight':'8', 'nine':'9'}
    word = ''
    result = ''
    for ch in s:
        if ch.isdigit():
            result += ch
        else:
            word += ch
            if word in num_dict:
                result += num_dict[word]
                word = ''
    return int(result)