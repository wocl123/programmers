#문제 : Lv2. 행렬의 곱셈
import numpy as np
def solution(arr1, arr2):
    answer = []
    A = np.array(arr1)
    B = np.array(arr2)
    result = np.dot(A,B)
    
    return result.tolist()

print(solution([[1,4], [3,2], [4,1]], [[3,3], [3,3]]))
print(solution([[2,3,2], [4,2,4], [3,1,4]], [[5,4,3], [2,4,1], [3,1,1]]))