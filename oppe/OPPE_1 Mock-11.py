def index_pos(Matrix,element):
    for r in Matrix:
        for c in r:  
            if c == element:
                return ([Matrix.index(r)+1, r.index(c)])

def is_reachable(grid):
    ant_pos = index_pos(grid,"B")
    food_pos = index_pos(grid,"G")

    if ant_pos[0] >= food_pos[0] and ant_pos[1]<=food_pos[1]:

        step = ant_pos[0]-food_pos[0] + food_pos[1]-ant_pos[1]
        return(True,step) 
    
    else:
        return(False,None)    
    