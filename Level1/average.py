#문제 : 평균 구하기

def solution(arr):
    
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    answer = sum / len(arr)
    return answer

arr1 = [1,2,3,4]
arr2 = [5,5]

print(solution(arr1))
print(solution(arr2))
