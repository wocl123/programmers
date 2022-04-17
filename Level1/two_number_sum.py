#문제 : 두 정수 사이의 합

#첫번째 풀이
def solution(a,b):
    sum = 0
    if a > b:
        for i in range(b, a+1): sum+= i
    else:
        for i in range(a, b+1): sum+= i
    return sum

#두번째 풀이
def solution2(a,b):
    if a > b: a, b = b, a
    
    return sum(range(a, b+1))

a1 = 3
a2 = 3
a3 = 5

b1 = 5
b2 = 3
b3 = 3

print(solution(a1,b1))
print(solution(a2,b2))
print(solution(a3,b3))
print(solution2(a1,b1))
print(solution2(a2,b2))
print(solution2(a3,b3))
