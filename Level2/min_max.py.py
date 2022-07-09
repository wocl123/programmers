#문제 : Lv2. 최댓값과 최솟값

def solution(s):
    answer = list(map(int, s.split(" ")))

    answer.sort()
    return str(answer[0]) + ' ' + str(answer[-1])

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))