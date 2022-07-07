#문제 : 다음 큰 숫자

def solution(n):
    num1 = format(n, 'b')
    cnt1=0
    i = 1
    for j in range(len(num1)):
        if num1[j] == "1":
            cnt1 += 1

    while(True):
        cnt2 = 0
        num2 = format(n + i, 'b')
        for k in range(len(num2)):
            if num2[k] == "1":
                cnt2 += 1
        if cnt1 == cnt2:
            return int(num2, 2)
        i += 1

def solution2(n):
    num1 = bin(n).count('1')
    
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n        

print(solution(78), solution(15))
print(solution2(78), solution2(15))
