def solution(array, commands):
    answer = []
   
    for i in range(len(commands)):
        result = array[commands[i][0]-1 : commands[i][1]]
        result.sort()
        temp = commands[i][2]
        answer.append(result[temp-1])
    return answer

def solution2(array,commands):
    answer = []
    
    for co in commands:
        i,j,k = co
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))
print(solution2([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))