from collections import Counter

def solution(participant, completion):
    part_counter = Counter(participant)
    com_counter = Counter(completion)
    not_com = part_counter - com_counter
    
    return list(not_com.keys())[0]