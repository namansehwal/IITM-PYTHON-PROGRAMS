a = input().split(',')
list = ['A','B','C','D']
mode = 0 
mode_element = ''

for e in list:
  element_count = a.count(e)
  if mode < element_count:
    mode = element_count
    mode_element = e


    
print('Occurences of A is',a.count('A'))
print('Occurences of B is',a.count('B'))
print('Occurences of C is',a.count('C'))
print('Occurences of D is',a.count('D'))
print('Sum of all Occurences is', len(a))
print('Mode is', mode_element, 'with occurences', mode)