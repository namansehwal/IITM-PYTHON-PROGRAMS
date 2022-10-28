m=int(input())

station_dict={}

for i in range(m):
  n=input()
  p=int(input())
  
  dic={}
  for i in range(p):
    
    s=input().split(',')
    dic[s[0]]=int(s[1])
  station_dict[n]=dic
