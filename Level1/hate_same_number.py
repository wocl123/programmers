#문제 : 같은 숫자는 싫어

def solution(arr):
    answer = []
    num = -1
    for i in arr:
        if i != num:
            num = i
            answer.append(num)
    
    return answer

def solution2(arr):
    answer = []
    for i in arr:
        if (len(answer) == 0) or (answer[-1] != i):
            answer.append(i)
    return answer

arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

print(solution(arr1))
print(solution(arr2))

print(solution(arr1))
print(solution(arr2))
