#문제 : 행렬의 덧셈
import numpy as np
#첫번째 풀이
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[i])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    return answer

#두번째 풀이
def solution2(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
    answer = A+B
    return answer.tolist()

fi_arr1 = [[1,2], [2,3]]
fi_arr2 = [[1], [2]]

se_arr1 = [[3,4], [5,6]]
se_arr2 = [[3], [4]]

print(solution(fi_arr1, se_arr1))
print(solution(fi_arr2, se_arr2))

print(solution2(fi_arr1, se_arr1))
print(solution2(fi_arr2, se_arr2))
