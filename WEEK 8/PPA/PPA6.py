for _ in range(1):
    
 test_cases = int(input())-1
 sample = set()
 
 three_multiple = test_cases//3
 three_sum = (three_multiple*(3+three_multiple*3))//2
 
 five_multiple = test_cases//5
 five_sum = (five_multiple*(5+five_multiple*5))//2

 fifteen_multiple = test_cases//15
 fifteen_sum = (fifteen_multiple*(15+fifteen_multiple*15))//2

 final_sum = three_sum + five_sum - fifteen_sum

 print(three_sum, five_sum, fifteen_sum, final_sum)
 
             
        

 