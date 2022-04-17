#문제 : 최솟값 만들기

def solution(a, b):
    a.sort()
    b.sort(reverse = True)
    sum = 0
    for i, j in zip(a, b):
        sum += i*j
    
    return sum

print(solution([1,4,2], [5,4,4]))
print(solution([1,2], [3,4]))