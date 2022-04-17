#문제 : 모의고사

def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0, 0, 0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == supo1[i%len(supo1)]:
            result[0] += 1
        if answers[i] == supo2[i%len(supo2)]:
            result[1] += 1
        if answers[i] == supo3[i%len(supo3)]:
            result[2] += 1   
    
    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i+1)
        
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
