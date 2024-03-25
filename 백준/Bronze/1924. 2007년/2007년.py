import sys
import datetime
weekday_list = {0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
month, day = map(int,sys.stdin.readline().split())
weekday = datetime.date(2007,month, day)
print(weekday_list[weekday.weekday()])