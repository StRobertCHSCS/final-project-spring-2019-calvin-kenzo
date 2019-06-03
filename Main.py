import time
countdown=True
time=120
while countdown == True:
    time = time-1
    time.sleep(1.0)
    print (time)
    countdown=True
    if time == 0:
        print ("Time is Up")
