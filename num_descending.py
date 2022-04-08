#문제 : 정수 내림차순으로 배치하기

def solution(n):
    st = list(str(int(n)))
    st.sort(reverse = True)

    return int("".join(st))

n = 118372

print(solution(n))