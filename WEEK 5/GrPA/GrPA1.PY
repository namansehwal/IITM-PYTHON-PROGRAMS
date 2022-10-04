# import random

# list = [[],[],[]]

# for j in range(3):
#    #sample(list, k) returns a list of k elements from the list
#    psuedolist = random.sample(range(1, 50), 10)    
#    list.append(psuedolist)

# for j in range(3):
#     print(sorted(list[j]))
#     flag = True
#     for i in range(10):
#         if j<2:
#             if list[j][i] in list[j+1]:
#                 print("There is a repetition of the number", list[j][i])
#                 flag = False
#     if flag:
#         print("There are no repetitions")




# import random
import random
# create a list
l = []
#j = 0
# iterate in the range that you wnat it to iterate
for j in range(3):
   
   for i in range(10):
        l.append(random.randint(1, 10))
         
print(l)   
# j = j + 1 
# check if there is any repetiton of the number
# for j in range(3):
#   print(sorted(l))
#   i = 0
#   flag = 0
#   while (i < len(l[j])-1):
#     if (l[j][i] == l[j][i + 1]):
#        print(l[j][i], l[j][i + 1])
#        flag = flag  + 1
#        print("Repetition exist")
#     i = i + 1
#   if (flag == 0):
#      print("Repetition does not exist")
# j = j + 1
# sequence : list, numbers repeated, comment (Repeated, Not repeated)