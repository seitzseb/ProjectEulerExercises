import datetime

count = 0
for year in range(1901,2001):
    for month in range(1,13):
        print(month)
        day = datetime.date(year,month,1).weekday()
        if day == 6:
            count+=1
print(count)