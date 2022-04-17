#문제 : 음양 더하기
def solution(absolutes, signs):
    sum = 0
    
    for i, j in zip(absolutes, signs):
        if j == False:
            i = -i
        sum += i
    
    return sum

absolutes1 = [4,7,12]
absolutes2 = [1,2,3]

signs1 = [True, False, True]
signs2 = [False, False, True]

print(solution(absolutes1, signs1))
print(solution(absolutes2, signs2))
