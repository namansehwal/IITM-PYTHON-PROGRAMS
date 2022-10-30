# First, we will take the input:  
lower_value = (input ("Please, Enter the Lowest Range Value: "))  
upper_value = (input ("Please, Enter the Upper Range Value: "))  
count=0

print ("The Prime Numbers in the range are: ") 
if type(int(lower_value)) == int and type(int(upper_value)) == int:
    lower_value=int(lower_value)
    upper_value=int(upper_value)
    for number in range (lower_value, upper_value + 1):  
    #if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:
                break  
        else:  
            print (number) 
            count=count+1
else:
  print("invalid_imput")
print("total number of prime numbers in the given range is" , count)