#문제 : 비밀지도

def solution(n, arr1, arr2):
    answer = []
    result = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)
    
    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                temp += '0'
            else:
                temp += '1'
        answer.append(temp)
    
    for i in range(n):
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')
    return answer

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))

"""
[0] = "#" "#" "#" "#" "#"
[1]
[2]
[3]
[4]
"""