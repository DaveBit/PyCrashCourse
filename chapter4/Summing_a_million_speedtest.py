
import time

start_time = time.time()
million2 = list(range(1, 1000001))
print(min(million2))
print(max(million2))
print(sum(million2))
print("---%s seconds---" % (time.time() - start_time))

start_time = time.time()
million3 = []
for number in range(1, 1000001):  # [number for number in range(1, 1000001)]
    million3.append(number)
print(min(million3))
print(max(million3))
print(sum(million3))
print("---%s seconds---" % (time.time() - start_time))

start_time = time.time()
million = [number for number in range(1, 1000001)]  # makes sense when having to use the number somehow. f.e number**2
print(min(million))
print(max(million))
print(sum(million))
print("---%s seconds---" % (time.time() - start_time))
