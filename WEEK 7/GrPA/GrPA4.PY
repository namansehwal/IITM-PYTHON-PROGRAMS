station_dict = {}
def dict_maker():
    #train name
    train_name = input()
    station_dict[train_name] = {}
    
    #stops 
    stops = int(input())
    
    for i in range(stops):
        
       station_name = input().split(',')
       station_dict[train_name][station_name[0]] = int(station_name[1])

for _ in range(int(input())):
    dict_maker()
    