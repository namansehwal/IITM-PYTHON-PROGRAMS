from curses.ascii import isalpha


string = input()
if 7< len(string) < 33:
    if isalpha(string[0]):
       if  ('s' and 'y') in string:
             print('hello')