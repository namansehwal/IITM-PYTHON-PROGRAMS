# Accept a string as input and print the vowels present in the string 
# in alphabetical order. If the string doesn't contain any vowels, 
# then print the string none as output. Each vowel that appears in the 
# input string — irrespective of its case — should appear just once in 
# lower case in the output.

#Code

string = input().lower()
output = ''

if 'a' in string:
    output += 'a'
if 'e' in string:
    output += 'e'
if 'i' in string:
    output += 'i'
if 'o' in string:
    output += 'o'
if 'u' in string:
    output += 'u'
if output == '':
    output = 'none'                    

print(output)
     