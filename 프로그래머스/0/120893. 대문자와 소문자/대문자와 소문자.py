def solution(my_string):
    lst = []
    for i in my_string:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        lst.append(i)
        
    
    return "".join(lst)