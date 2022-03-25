import datetime

time_now = datetime.datetime.now()
print(time_now)
print("Year :", time_now.strftime("%y"),time_now.strftime("%Y"),time_now.year)
print("Month:", time_now.strftime("%m"),time_now.strftime("%b"),time_now.strftime("%B"),time_now.month)
print("Day  :", time_now.strftime("%d"),time_now.strftime("%a"),time_now.strftime("%A"),time_now.day)
print(time_now.strftime("%H"),time_now.strftime("%M"),time_now.strftime("%S"))
print(time_now.strftime("%I"),time_now.strftime("%M"),time_now.strftime("%S"),time_now.strftime("%p"))
print(time_now.strftime("%d-%b-%Y %H:%M:%S.%f"))
print(time_now.date())
print(time_now.time())
print(time_now.hour)
print(time_now.minute)
print(time_now.second)
print(time_now.microsecond)
print(time_now.min)
print(time_now.max)



