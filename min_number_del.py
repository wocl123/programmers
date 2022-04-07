#문제 : 제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    
    if arr:
        return arr
    
    return [-1]

arr1 = [4,3,2,1]
arr2 = [10]

print(solution(arr1))
print(solution(arr2))