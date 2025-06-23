def solution(people, limit):
    people.sort()             # 오름차순 정렬
    left = 0                  # 가장 가벼운 사람
    right = len(people) - 1   # 가장 무거운 사람
    answer = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1         # 둘 다 태움
        # 무거운 사람은 항상 보트에 태움
        right -= 1
        answer += 1

    return answer
