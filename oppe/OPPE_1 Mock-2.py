input = list(map(int,input().split(',')))

len = len(input)//2

left = sum(input[0:len])
right = sum(input[-len])

if left == right:
    print('balanced')
elif left>right:
    print('left-heavy')
else:
    print('right-heavy')











sample_input = input().split(',')
for x in range(len(sample_input)):
    sample_input[x] = int(sample_input[x])

#[1, 2, 3, 4, 5, 6]
half_len = len(sample_input)//2

left_weight = sum(sample_input[0:half_len])
right_weight = sum(sample_input[half_len:])


if left_weight> right_weight:
  print('left-heavy')
elif left_weight < right_weight:
  print('right-heavy')
else:
  print('balanced')
