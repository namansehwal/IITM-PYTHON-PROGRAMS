#check pythagorean triplets
def pythagoreanTriplets(l):
     for i in range(len(l)):
          for j in range(i+1,len(l)):
               for k in range(j+1,len(l)):
                    if l[i]**2 + l[j]**2 == l[k]**2:
                         return True
     return False
print(pythagoreanTriplets([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))     