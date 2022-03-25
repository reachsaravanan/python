"""
Accept user input for MONTH, YEAR
Print calendar for given MONTH, YEAR
"""
import calendar
user_Month = input("Enter The Month Number [1..12]\t:")
user_year = input("Enter The Year Number [9999]\t:")
user_calendar = calendar.monthcalendar(int(user_year), int(user_Month))
for x in user_calendar:
    print(x)

