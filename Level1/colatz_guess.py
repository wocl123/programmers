#문제 : 콜라츠 추측

def solution(num):
    count = 0
    while(num!=1):
        if num%2==0:
            num = num/2
            count += 1
        else:
            num = num*3 + 1
            count += 1
    if count > 500:
        count = -1
    return count

n1 = 6
n2 = 16
n3 = 626331

print(solution(n1))
print(solution(n2))
print(solution(n3))
