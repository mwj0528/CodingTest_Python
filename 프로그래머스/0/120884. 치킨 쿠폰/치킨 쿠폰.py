# # 100 / 10 = 10
# # 10 / 10 = 1
# # 1 / 10 = 0 ... 1

# # 1081 / 10 = 108 ... 1
# # 108 / 10 = 10 ... 8
# # 10/ 10 = 1
# # 1 / 10 = 0 ... 1

# # chicken 108 10 1
# # answer 108 + 10 + 1 
# # coupon 8 + 1 + 0

def solution(chicken):
    answer = 0
    coupon = 0
    
    while chicken > 0:
        coupon += chicken % 10
        answer += coupon // 10
        coupon //= 10
        chicken //= 10
        answer += chicken
    return answer

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10 # 서비스 주문하는 치킨 개수 = 받은 쿠폰 수
        mod = chicken % 10 # 서비스 주문 후 남은 쿠폰 수
        answer += div # 치킨 주문 누적 수
        chicken = div+mod # 전체 쿠폰 수
    return answer
    
        
 