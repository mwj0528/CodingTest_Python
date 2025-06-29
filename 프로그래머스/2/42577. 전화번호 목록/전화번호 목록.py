def solution(phone_book):
    phone_set = set(phone_book)  # 해시셋으로 변환 (탐색 O(1))
    
    for number in phone_book:
        # 접두사를 한 글자씩 증가시키며 확인
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_set:
                return False  # 다른 번호가 접두사인 경우
    return True
