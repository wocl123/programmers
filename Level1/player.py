#문제 : 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]

participant1 = ["leo", "kiki", "eden"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participant3 = ["mislav", "stanko", "mislav", "ana"]

completion1 = ["eden", "kiki"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
completion3 = ["stanko", "ana", "mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))
