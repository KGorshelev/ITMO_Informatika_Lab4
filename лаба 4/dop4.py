import time

import task1
import dop1
import dop2
#import dop3


start = time.time()
for i in range(100):
    task1.main()
end = time.time()  
print(f"task0: {end-start}s") 


start = time.time()
for i in range(100):
    dop1.main()
end = time.time()  
print(f"task1: {end-start}s")


start = time.time()
for i in range(100):
    dop2.main()
end = time.time()  
print(f"task2: {end-start}s")


#start = time.time()
#for i in range(100):
#    dop3.main()
#end = time.time()
#print(f"task3: {end-start}s")