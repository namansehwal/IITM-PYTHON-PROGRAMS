string = input()
n1 = int(input())
n2 = int(input())

sub_str = string[n1:n2 + 1]
length = len(sub_str)

print(sub_str * (len(string) // length + 1))