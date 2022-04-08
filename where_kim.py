#문제 : 서울에서 김서방 찾기

def solution(seoul):
    answer = list(seoul)
    a = answer.index("Kim")
    
    return "김서방은 {}에 있다.".format(a)

seoul = ["Jane", "Kim"]
seoul2 = ["Jane", "Tomas", "Kim"]

print(solution(seoul))
print(solution(seoul2))