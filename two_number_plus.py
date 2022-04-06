#문제 : 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i]+numbers[j]
            if sum not in answer:
                answer.append(sum)
    answer.sort()
    return answer

numbers1 = [2,1,3,4,1]
numbers2 = [5,0,2,7]

print(solution(numbers1))
print(solution(numbers2))