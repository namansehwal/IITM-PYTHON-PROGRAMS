n = int(input())
L = [ ]
for i in range(n):
    L.append(input())
point = input().split(',')
x = int(point[0])
y = int(point[1])
min_list = []
min_dist = 1000
for i in range(n):
    temp = L[i].split(',')
    temp_x = int(temp[0])
    temp_y = int(temp[1])
    dist = ((x - temp_x) ** 2 + (y - temp_y) ** 2) ** 0.5
    if (dist < min_dist):
        min_dist = dist
        min_list = [L[i]]
    elif dist == min_dist:
        min_list.append(L[i])
for point in min_list:
    print(point)