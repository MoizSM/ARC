import sys
import json
import numpy as np

def solve():
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f)

    grid = np.asarray(data['test'][0]['input'])
    count = 0
    for x in np.nditer(grid):
        if x!=0 :
            count = count + 1
    print(grid)

    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if ( i == 0 and x < count ):
                grid[i][x] = 2
            else:
                grid[i][x] = 0
            if (count > 3):
                grid[1][1]= 2
    
    print(grid)
        

solve()