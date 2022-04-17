#문제 : 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    count1 = count2 = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count1 += 1

    for i in range(len(lottos)):
        if (lottos[i] == 0) and (lottos[i] not in win_nums):
            lottos[i] = win_nums[i]
        if lottos[i] in win_nums:
            count2 += 1
    
    high_rank = answer[count2]
    low_rank = answer[count1]
    
    return [high_rank, low_rank]
    
    

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

lottos2 = [0,0,0,0,0,0]
win_nums2 = [38,19,20,40,15,25]

lottos3 = [45,4,35,20,3,9]
win_nums3 = [20,9,3,45,4,35]

print(solution(lottos, win_nums))
print(solution(lottos2, win_nums2))
print(solution(lottos3, win_nums3))
