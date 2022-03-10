import random

deathLimit, birthLimit = 4, 1
chance_alive = 4
steps = 5
SIZEMAP = 600
def create_map():
    
    MAP = []
    for i in range(SIZEMAP):
        MAP.append([0 for y in range(SIZEMAP)])
    for i in range(SIZEMAP):
        for y in range(SIZEMAP):
            if random.uniform(0, 10) < chance_alive:
                MAP[i][y] = 1 
            else:
                MAP[i][y] = 0
    for i in range(steps):
        MAP = doSimulationStep(MAP)
    return MAP



##Returns the number of cells in a ring around (x,y) that are alive.
def countAliveNeighbours( map,  x,  y):
    count = 0
    for i in range(2):
        for j in range(2):
            neighbour_x = x+i
            neighbour_y = y+j
            #If we're looking at the middle point
            if i == 0 and j == 0:
                ##Do nothing, we don't want to add ourselves in!
                pass
            ##In case the index we're looking at it off the edge of the map
            elif neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(map) or neighbour_y >= len(map[0]):
                count += 1
            
            #Otherwise, a normal check of the neighbour
            elif map[neighbour_x][neighbour_y]:
                count += 1
    return count

def  doSimulationStep( oldMap):
    newMap = oldMap
    ##Loop over each row and column of the map
    for x, row in enumerate(oldMap):
        for y, cell in enumerate(row):
            nbs = countAliveNeighbours(oldMap, x, y)
            ##The new value is based on our simulation rules
            ##First, if a cell is alive but has too few neighbours, kill it.
            if nbs:
                if oldMap[x][y] :
                    if nbs < deathLimit:
                        newMap[x][y] = 0
                    
                    else:
                        newMap[x][y] = 1
                    
                ##Otherwise, if the cell is dead now, check if it has the right number of neighbours to be 'born'
                else:
                    if nbs > birthLimit:
                        newMap[x][y] = 0
                    
                    else:
                        newMap[x][y] = 1
    return newMap
