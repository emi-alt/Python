from datetime import date, time, datetime 
today = date.today()
now = datetime.now()
print(f"Today's date is {today}")
print(f"The current time is {now}")

print(f"Datetime components are: {today.day} - {today.month} - {today.year}")