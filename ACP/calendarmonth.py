import calendar
cal = calendar.month_name
i = 1
for i in range(0,13):
    i += 1
    print(cal[i])
    if i == 12:
      break