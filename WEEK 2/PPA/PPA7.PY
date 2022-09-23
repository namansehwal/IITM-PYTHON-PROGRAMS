# A sequence of five words is called magical if the i^{th}ith word 
# is a substring of the (i + 1)^{th}(i+1)th word for every ii in 
# the range 1 \leq i < 51≤i<5. Accept a sequence of five words as 
# input, one word on each line. Print magical if the sequence is 
# magical and non-magical otherwise. Note that str_1 is a substring 
# of str_2 if and only if str_1 is present as a sequence of consecutive 
# characters in str_2.
i = input()
i2 = input()
i3 = input()
i4 = input()
i5 = input()

if (i5[0:4] == i4) and (i4[0:3] == i3) and (i3[0:2] == i2) and (i2[0:1] == i):
    print('magical')
else:
    print('non-magical')    