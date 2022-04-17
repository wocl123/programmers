#문제 : 최대공약수와 최소공배수

def solution(n, m):
    
    answer = []
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a,b):
        return (a*b) // gcd(a,b)
    
    g_cd = gcd(n, m)
    l_cm = lcm(n, m)
    
    return [g_cd, l_cm]

print(solution(3, 12))
print(solution(2, 5))
