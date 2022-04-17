#문제 : 소수 만들기

def is_prime(num):
    
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
            
def solution(nums):
    count = 0
    
    for i in range(len(nums)-2):
        sum = 0
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime(sum):
                    count += 1
    return count

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))


"""
1+2+3 = 0 1 2
1+2+4 = 0 1 3
1+3+4 = 0 2 3
2+3+4 = 1 2 3

1+2+7 = 0 1 2
1+2+6 = 0 1 3
1+2+4 = 0 1 4 
2+7+6 = 1 2 3
2+7+4 = 1 2 4
2+6+4 = 2 3 4
"""
