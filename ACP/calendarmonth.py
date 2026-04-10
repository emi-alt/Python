import calendar
cal = calendar.month_name
i = 0
print(cal[1])
for i in range(1,13):
    i += 1
    print(cal[i])
    if i == 12:
      break