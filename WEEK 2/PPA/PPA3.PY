T = int(input())
if T<0 or T>=24:
    print('INVALID')
elif 0<=T<=5:
    print('NIGHT')
elif 6<=T<=11:
    print('MORNING') 
elif 12<=T<=17:
    print('AFTERNOON')
elif 18<=T<=23:
    print('EVENING')


