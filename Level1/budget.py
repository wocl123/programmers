#문제 : 예산

def solution(d, budget):
    answer = 0
    d_value = sorted(d)
    for i in d_value:
        budget -= i
        if budget <0:
            break
        answer += 1
                
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
