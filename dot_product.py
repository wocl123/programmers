def solution(a, b):
    sum = 0
    
    for i, j in zip(a,b):
        sum += i*j
    
    return sum

a1 = [1,2,3,4]
a2 = [-1,0,1]

b1 = [-3,-1,0,2]
b2 = [1,0,-1]

print(solution(a1, b1))
print(solution(a2, b2))