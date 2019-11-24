import sys
import json
import numpy as np

def solve():
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f)

    #PLAYGROUND
    # for i in range(len(data)):
    #     x = np.asarray(data['train'][i]['input'])
    #     print(x,'\n')

    ##################################

    # PROGRAM ################################
    grid = np.asarray(data['test'][0]['input'])
    for i in range(len(grid)):
        checkVal = grid[i][0]
        check = True
        for j in grid[i]:
            if (checkVal!= j):
                check = False
        if (check == True):
            grid[i] = 5
        else:
            grid[i] = 0
    print(grid)
    #########################################  

solve()
