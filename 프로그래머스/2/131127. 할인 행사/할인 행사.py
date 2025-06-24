# want: 바나나3, 사과2, 쌀2, 돼지고기2, 냄비1
# discount: 치킨 사과 사과 바나나 쌀 사과 돼지고기 바나나 돼지고기 쌀 냄비 바나나 사과 바나나
from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_dic = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        counter = Counter(discount[i:i+10])
        
        if counter == want_dic:
            answer += 1
    
    return answer

# from collections import Counter

# def solution(want, number, discount):
#     answer = 0
#     check = dict(zip(want, number))
    
#     for i in range(len(discount)-9):
#         c = Counter(discount[i:i+10])
#         if c == check:
#             answer += 1

#     return answer