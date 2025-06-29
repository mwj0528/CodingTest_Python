def solution(genres, plays):
    answer = []
    dic = {} # {장르 : [(플레이 횟수, 고유번호)]}
    playdic = {} # {장르 : 총 재생 횟수}
    
    for i in range(len(genres)):
        playdic[genres[i]] = playdic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]
    
    genre_sort = sorted(playdic.items(), key = lambda x: x[1], reverse = True)
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, total_play) in genre_sort:
        dic[genre] = sorted(dic[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (_,idx) in dic[genre][:2]]
    return answer