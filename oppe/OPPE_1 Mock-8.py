def exactly_two(players):
    
    All_players = []
    for player in players:
        # print(player)
        count = 0
        for i in players[player]:
            
            if players[player][i]==True:
                count+=1
        if count==2:
            All_players.append(player)
    return(set(All_players))
    