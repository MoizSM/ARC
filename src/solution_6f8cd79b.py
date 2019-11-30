import sys
import json
import numpy as np 


def solve(): #Logic Funtion
    with open(sys.argv[1] , 'r') as f:
        dataset = json.load(f) # Parsing the JSON file
    var = ['train' , 'test'] 
    # Running for all the training and testing inputs  
    for x in var: 
        for n in range(len(dataset[x])): 
            gridData = np.asarray(dataset[x][n]['input'])         
            for i in range(len(gridData)): # Getting the Grids in form of rows
                if ((i==0) or i == len(gridData)-1): # Comparing if current row is first or last row of the grid
                    gridData[i] = 8 # Coloring each the row if current row is first or last 
                else: 
                    for _ in gridData[i]: # for all the elements of row 
                        gridData[i][0] = 8 # Coloring the first element of the row
                        gridData[i][-1] = 8 # Coloring the last element of the row
            print(gridData, '\n') #Printing the output grids

solve()

