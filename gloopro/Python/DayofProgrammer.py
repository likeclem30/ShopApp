"""Abigail invented a Time Machine and wants to test it by time-traveling to visit Wakanda on the Day of the Programmer. Each year, the day of the programmer is determined. It can be any day during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Wakanda's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Wakanda.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

Divisible by 400
Divisible by 4 and not divisible by 100
Given a year, y, find the date of the 256th day of that year according to the official Wakanda's calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is y.

For example, the given year = 1984 and day = 256. 
1984 is divisible by 4, so it is a leap year. 
The 256th day of a leap year after 1918 is September 12, 
so the answer is 12.09.1984."""

#leapyear = year%day
    # 1-if leapyear is true:
    # 2-Days in a year = 366
    #3- dateOF the year = 365 + 256 = 110
    #4 - new date 110 + 256 = 366 = 31st December of the next year(always same)

def DayOfProgrammer(year,day):
    if year%4 ==0 and year%100 !=0:
        print("Is a leap year")
        if day <= 31:
            print(31-(31-day),".01.",year)

        if day <= 60 and day >31:
            print(day-31,".02.",year)

        if day <= 91 and day> 60:
            print(day-60,".03",year)

        if day <= 121 and day> 91:
            print(day-91,".04.",year)

        if day <= 152 and day> 121:
            print(day-121," .05 ",year)

        if day <= 182 and day> 152:
            print(day-152," .06. ",year)

        if day <= 213 and day> 182:
            print(day-182,".07. ",year)

        if day <= 244 and day> 213:
            print(day-213,".08.",year)

        if day <= 274 and day> 244:
            print(day-244,".09.",year)
        
        if day <= 305 and day> 274:
            print(day-274,".10.",year)

        if day <= 335 and day> 305:
            print(day-305,".11.",year)

        if day <= 366 and day> 335:
            print(day-335,".12.",year)
    else:
        print(year,"is not a leap year")
    
DayOfProgrammer(1984,256)
    
    