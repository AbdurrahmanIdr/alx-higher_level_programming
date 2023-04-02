#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak
import random
import time

print(find_peak([1, 4, 6, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
a = list(range(1, 5000000))
a1 = list(range(4999999, 1, -1))
a2 = list(range(1, 5000000))
print("list set---")
random.shuffle(a2)
print("shuffled.......")
answers = [4999999]

avg_time = 0
timediff = time.time()
print("----verbose---")
for j in range(10):
    start_time = time.time()
    print(start_time - timediff)
    
    for i in range(10):
        res = find_peak(a)
        if res not in answers:
            print("Wrong answer {}".format(res))
            exit(1)
    print(time.time() - timediff)

    for i in range(10):
        res = find_peak(a1)
        if res not in answers:
            print("Wrong answer 2 {}".format(res))
            exit(1)
    print(time.time() - timediff)

    for i in range(10):
        find_peak(a2)
    print(time.time() - timediff)
    
    end_time = time.time()
    avg_time += (end_time - start_time)
    print("round eneded at: ", end="")
    print(end_time - timediff)

avg_time = avg_time / 10    

if avg_time > 5.0:
    print("Too slow")
    exit(1)

print("OK", end="")

