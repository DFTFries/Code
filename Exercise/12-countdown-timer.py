import time

countdown = int(input("Enter the time in seconds: "))


for x in range(countdown, 0, -1):                   # step -1 to count backwards
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)                                   # program sleeps for 1s, hence creating a timer

print("Time is up!")