import time

# epoch time
epochTime = time.time()
print(epochTime)

# get time tuple
timeTuple = time.localtime(epochTime)
print(timeTuple)
print("Year:", timeTuple[0])
print("Month:", timeTuple[1])
print("Day:", timeTuple[2])
print("Hour:", timeTuple[3], "Min:", timeTuple[4], "Sec:", timeTuple[5])
print("Day of week:", timeTuple[6])
print("Day of year:", timeTuple[7])
print("Is DST? :", timeTuple[8])

# get time in readable format
myTime = time.asctime(timeTuple)
print(myTime)

print("Year:", time.strftime("%Y", timeTuple))
print("Month:", time.strftime("%m", timeTuple))
print("Day:", time.strftime("%d", timeTuple))
print("Hour:", time.strftime("%H", timeTuple))
print("Min:", time.strftime("%M", timeTuple))
print("Sec:", time.strftime("%S", timeTuple))
print("AM/PM:", time.strftime("%p", timeTuple))

