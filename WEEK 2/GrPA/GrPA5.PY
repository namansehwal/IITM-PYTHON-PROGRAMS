string = input()
if 7< len(string) < 33:
    if string[0].isalpha():
       if ('/'not in string  and '='not in string and '"'not in string and '\"'not in string and "'" not in string and ' ' not in string)  :
          print(True)    
       else:
         print(False)
    else:
      print(False)
else:
   print(False)
    


             