#문제 : 2016년
from datetime import datetime

def solution(a, b):
    dateDict = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    
    date = '2016-{}-{}'.format(a,b)
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    
    return dateDict[datetime_date.weekday()]

print(solution(5, 24))
