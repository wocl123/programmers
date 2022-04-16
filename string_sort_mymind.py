#문제 : 문자열 내 마음대로 정렬하기

def solution(strings, n):
    
    answer = []
    result = []
    for i in range(len(strings)):
        result.append(strings[i][n]+strings[i])
    result.sort()
    
    for i in range(len(result)):
        answer.append(result[i][1:])
    return answer
    
    

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))