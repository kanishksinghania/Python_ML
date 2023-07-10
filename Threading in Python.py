import threading
from threading import *
import time
import math
def square(num):
  for i in num:
    time.sleep(3)
    print("Square:",i*i)
def cube(num):
  for i in num:
    time.sleep(3)
    print("Cube:",i*i*i)
def root(num):
  for i in num:
    time.sleep(3)
    print("Square Root:",pow(i,0.5))
#MAIN
num=[1,2,3,4,5,6,7,8]
t1=time.time()
thread1=threading.Thread(target=square,args=(num,))
thread2=threading.Thread(target=cube,args=(num,))
thread3=threading.Thread(target=root,args=(num,))
thread1.start()
time.sleep(2)
thread2.start()
time.sleep(2)
thread3.start()
thread1.join()
thread2.join()
thread3.join()
t2=time.time()
print("total time taken:",t2-t1)

'''Square: 1
Cube: 1
Square: 4
Square Root: 1.0
Cube: 8
Square: 9
Square Root: 1.4142135623730951
Cube: 27
Square: 16
Square Root: 1.7320508075688772
Cube: 64
Square: 25
Square Root: 2.0
Cube: 125
Square: 36
Square Root: 2.23606797749979
Cube: 216
Square: 49
Square Root: 2.449489742783178
Cube: 343
Square: 64
Square Root: 2.6457513110645907
Cube: 512
Square Root: 2.8284271247461903
total time taken: 28.090718746185303'''