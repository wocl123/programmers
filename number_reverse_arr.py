#문제 : 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    st = list(str(n))
    st.reverse()
    for i in st:
        answer.append(int(i))
    return answer

n = 12345

print(solution(n))