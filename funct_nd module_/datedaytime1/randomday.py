import random
import time
def randmt(start, end):
    print("Printing random date between ", start, " and ", end)
    randomdate = random.random()
    datefrmt = "%d/%m/%Y"

    starttime = time.mktime(time.strptime(start, datefrmt))
    endtime = time.mktime(time.strptime(end, datefrmt))

    randmtime = starttime + randomdate * (endtime - starttime)
    randomdate = time.strftime(datefrmt, time.localtime(randmtime))
    return randomdate
print("Random date generator: ", randmt("01/01/2020", "31/12/2020"))