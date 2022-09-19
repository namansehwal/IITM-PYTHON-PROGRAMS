dataset = {
    'B':'BattleShip',
    'C':'Cruiser',
    'D':'Destroyer',
    'F':'Frigate'
}

T = int(input())

for _ in range(T):
    alpha = input().capitalize()
    
    if alpha in dataset.keys():
        print(dataset[alpha])