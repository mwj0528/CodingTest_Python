def solution(id_pw, db):
    for cor in db:
        if cor == id_pw:
            return "login"
        elif cor[0] == id_pw[0]:
            return "wrong pw"
        
    return 'fail'