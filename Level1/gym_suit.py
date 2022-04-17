#문제 : 체육복

def solution(n, lost, reverse):
    set_reverse = set(reverse) - set(lost)
    set_lost = set(lost) - set(reverse)
    print(set_reverse, set_lost)
    for reverse in set_reverse:
        if reverse-1 in set_lost:
            set_lost.remove(reverse-1)
        elif reverse+1 in set_lost:
            set_lost.remove(reverse+1)
    print(set_lost)
    return n-len(set_lost)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))


"""
n = 학생의 수
lost = 해당 인원이 잃어버린 체육복 
reverse = 체육복의 여분이 있는 인원

Tip) 잃어버린 사람의 양 옆에 있어야 빌려줄 수 있음. => index로 찾아야함?

i) 1 0 1 0 1 len(lost) = 2 len(reverse) = 3
reverse = [1,0,1,0,1]
lost = [0,1,0,1,0]
reverse+lost = [1,1,1,1,1] = answer.count(1) = 5

ii) 1 0 1 0 1 len(lost) = 2 len(reverse) = 1
reverse = [0,0,1,0,0]
lost = [0,1,0,1,0]
reverse+lost = [0,1,1,1,0] = answer.count(1) = 3
    
iii) 1 1 0 
reverse = [1,0,0]
lost = [0,0,1]
reverse+lost = [0,1,1] = answer.count(1) = 2
"""
