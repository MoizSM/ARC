import sys
import json
import numpy as np 


def solve(): #Logic Funtion
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f) #Parsing the JSON file

        var = ['train' , 'test']
        #Running for all the training and testing inputs
        for x in var:
            for n in range(len(data[x])):  
                grid = np.asarray(data[x][n]['input'])
                print(grid)
                grid = np.rot90(grid)
                print(grid)
                grid = np.flipud(grid)
                print(grid,'\n')
solve()