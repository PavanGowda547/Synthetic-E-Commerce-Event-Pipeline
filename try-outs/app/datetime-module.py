from datetime import datetime, date, timedelta, timezone

# present date and time
now = datetime.now()
# today date
today = date.today()

print("Today Date : ", today)
print("Present Date and Time : ", now)

# UTC date and timestamps
now_utc = datetime.now(timezone.utc)
print("The present UTC date and time is : ", now_utc)

# creating specific dates
dt = datetime(2026, 10, 2, 15, 30, 0)
print("dt = datetime(2026, 10, 2, 15, 30, 0)")
print("The pre-defined date is : ", dt, "and it's data type is : ",type(dt))

# extracting specific part of the date and time
print()
print("Retrieving a part of date from the datetime object")
print("The present date and time is : ", now)
print("day : ", now.day)
print("month : ", now.month)
print("year : ", now.year)
print("hour : ", now.hour)
print("minute : ", now.minute)
print("second : ", now.second)

# calculating date and time using timedelta
print()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Calculate present date and time : ", today)
print("Yesterday date : ", yesterday)
print("Tomorrow date : ", tomorrow)

# creating date range
start = datetime(2026, 10, 1)
end = datetime(2026, 10, 5)

current = start

print()
print("Generating a date range : ")
while current <= end:
    print(current.date())
    current += timedelta(days=1)

# formatting dates using strftime()
dt = datetime.now()
print()
print("The actual date is : ", dt)
date_string = dt.strftime("%m-%d-%Y")
print("The formatted date after strftime() in [%m-%d-%Y] : ", date_string)

# parsing a string into datetime
date_string = "2026-10-03"
dt = datetime.strptime(date_string, "%Y-%m-%d")
print()
print("Before parsing a string into date : ", date_string, " and its data type is : ", type(date_string))
print("After parsing : ",dt)
print(type(dt))

# comapring dates with each other
date1 = datetime(2026, 10, 1)
date2 = datetime(2026, 10, 3)

print()
if date2 > date1:
    print(f"{date2} is greater than {date1}")
else:
    print(f"{date1} is greater than {date2}")

# calculating date age
created_at = datetime(2026, 9, 25)
now = datetime.now()

age = now - created_at
print()
print("Calculating the date age")
print("The created date : ", created_at)
print("The present date : ", now)
print("Difference between created and present : ",age)
