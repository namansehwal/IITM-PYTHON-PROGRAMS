total = int(input())
s1 =int(input())
s2 =int(input())
s3 =int(input())
 
if (s1 and s2 and s3) != 0:
    if (s1!=s2) and (s2!=s3) and (s3!=s1):
        if (s1+s2+s3 == total):
            print('FAIR')
        else:
            print('UNFAIR')    
    else:
            print('UNFAIR') 
else:
            print('UNFAIR')                     