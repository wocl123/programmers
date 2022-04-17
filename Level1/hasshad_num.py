#문제 : 하샤드 수

def solution(x):
    x = str(x)
    sum = 0
    for i in x:
        sum += int(i)
    if int(x)%sum == 0:
        return True
    else:
        return False
    #return True if int(x)%sum == 0 else False
arr1 = 10
arr2 = 12
arr3 = 11
arr4 = 13

print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
print(solution(arr4))
