input = input()
mistake = input.count('l') + input.count('o')

if mistake != 0:
    print(mistake, 'mistakes')
    
    print(input.replace('o', '0').replace('l','1'))
else:
    print('No mistakes')    