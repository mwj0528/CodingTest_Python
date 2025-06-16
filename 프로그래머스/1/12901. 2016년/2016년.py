def solution(a, b):
    calender = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = 0
    for i in range(1, a):
        day += calender[i]
    day += b
    answer = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    return answer[(day-1) % 7]