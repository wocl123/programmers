def solution(numbers):
    max_result = 45
    sum = 0
    for i in numbers:
        sum += i
    
    return (max_result - sum)

numbers1 = [1,2,3,4,6,7,8,0]
numbers2 = [5,8,4,0,6,7,9]

print(solution(numbers1))
print(solution(numbers2))