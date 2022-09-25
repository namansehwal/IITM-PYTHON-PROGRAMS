string = input()
if '.' in string and string.count('.') == 1 and string.replace('.','').isdigit() or 'e':
    print("Float")
elif string.isdigit():
    print("Integer") 
else:    
    print("None")        

