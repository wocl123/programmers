#문제 : 폰켓몬

def solution(nums):
    
    size = len(nums)//2
    arr = list(set(nums))
    
    if len(arr) > size:
        answer = size
    else:
        answer = len(arr)   
    
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))


"""
1. N마리의 폰켓몬 중에서 N/2 마리를 가져가도 좋음. = len(nums)//2
2. 같은 종류의 폰켓몬은 같은 번호를 가지고 있음.
"""
