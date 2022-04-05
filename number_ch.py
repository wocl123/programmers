def solution(s):
    eng = {"zero": 0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
           "seven":7, "eight":8, "nine":9}
    answer = ""
    length = len(s)
    result = ""
    
    for i in s:
        if i.isdigit():
            result += i
        else:
            answer += i
        
        if answer in eng.keys():
            result += str(eng[answer])
            answer = ""
    return result    
    

str1 = "one4seveneight"     #=> 1478
str2 = "23four5six7"        #=>234567
str3 = "2three45sixseven"   #=>234567
str4 = "123"                #=>123

print(solution(str1))
print(solution(str2))
print(solution(str3))
print(solution(str4))