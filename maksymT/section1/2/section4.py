year = int(input("enter a year: "))
if year%4 == 0 and year%100 !=00 or year%400 == 0:
 print(year, "is a leap year")
else:
 print(year, "is not leap year")
month = int(input("enter a month number:"))
if month < 0 or month > 0:
 print("invalid, enter another month")
 elif month == 1 or month == 3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12