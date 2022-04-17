#문제 : 최소직사각형

def solution(sizes):
    
    big_value = []
    small_value = []
    
    for i in sizes:
        if i[0] > i[1]:
            big_value.append(i[0])
            small_value.append(i[1])
        else:
            big_value.append(i[1])
            small_value.append(i[0])
    
    return max(big_value) * max(small_value)

print(solution([[60,50], [30,70], [60,30], [80,40]]))
print(solution([[10,7], [12,3], [8,15], [14,7], [5,15]]))
print(solution([[14,4], [19,6], [6,16], [18,7], [7,11]]))
