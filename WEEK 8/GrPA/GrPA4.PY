#calculate execution time of program

import time
start_time = time.time()

for _ in range(1):
    n = 100
    sum = 0
    n3 = (n-1)//3
    n5 = (n-1)//5

    for x in range(1,n3+1):
        sum = sum + 3*x
    for y in range(1,n5+1):
      e = 5*y
      if e%3!=0:
        sum = sum + e    
    print(sum)

end_time = time.time()
print(end_time,start_time)