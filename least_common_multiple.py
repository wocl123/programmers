#문제 : N개의 최소공배수

def solution(arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a,b):
        return (a*b) // gcd(a,b)
    
    lcm_result = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        lcm_result = lcm(lcm_result, arr[i])
    
    return lcm_result
    

print(solution([2,6,8,14]))
print(solution([1,2,3]))