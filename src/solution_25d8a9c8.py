import sys
import json
import numpy as np

def solve():
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f)

    var = ['train' , 'test']
    for x in var:
        for n in range(len(data[x])):
            grid = np.asarray(data[x][n]['input'])
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
            print(grid , '\n')

solve()
