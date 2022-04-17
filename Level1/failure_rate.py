#문제 : 실패율

def solution(N, stages):
    stages.sort()
    result = [0]*(N+1)
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        if stages.count(i):
            result[i] = stages.count(i) / length
            length -= stages.count(i)
        answer.append((i, result[i]))
    answer = sorted(answer, key=lambda x: x[1], reverse= True)
    print(answer)
    answer = [i[0] for i in answer]
    return answer
    

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
