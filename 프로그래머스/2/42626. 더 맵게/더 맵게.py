import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    cnt = 0
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        food_1 = heapq.heappop(heap)
        food_2 = heapq.heappop(heap)
        food = food_1 + (food_2 * 2)
        heapq.heappush(heap, food)
        cnt += 1
  
    return cnt
