results = [ ]
for i in range(8):
    L = input().split(',')
    winner = L[0] # the first team is the winner
    losers = L[1: ] # all these teams have lost to the winner
# we only need the number of wins and the winning team
    results.append((winner, len(losers)))

table = [ ]
# two-level-sort
# refer GrPA-4 of week-6
# we first sort by points, then by name
while results != [ ]:
    maxteam = results[0]
    for i in range(len(results)):
        team = results[i]
        if team[1] > maxteam[1]:
            maxteam = team
        elif team[1] == maxteam[1] and team[0] < maxteam[0]:
            maxteam = team
    results.remove(maxteam)

    table.append(maxteam)
for team in table:
    print(f'{team[0]}:{team[1]}')