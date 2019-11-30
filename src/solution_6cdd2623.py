import sys
import json
import numpy as np 


def solve(): #Logic Funtion
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f) #Parsing the JSON file

    grid = np.asarray(data['train'][0]['input'])
    var = ['train' , 'test']
    #Running for all the training and testing inputs
    for x in var:
        for n in range(len(data[x])):  
            grid = np.asarray(data[x][n]['input'])
            
            storeCol = 0
            for c in range(grid.shape[1]):
                if(grid[0][c] != 0):
                    if(grid[0][c] == grid[grid.shape[0]-1][c]):
                        storeCol = c #Storing the column that have the same first and last color
                        for l in range(grid.shape[0]):
                            grid[l][c] = grid[0][c] #Changing all the colors of that column to that particular color
            storeRow = []            
            for r in range(grid.shape[0]):
                if(grid[r][0] != 0):
                    if(grid[r][0]==grid[r][grid.shape[1]-1]):
                        storeRow.append(r) # Storing the rows that have the same first and last color
                        for k in range(grid.shape[1]):
                            grid[r][k] = grid[r][0] # Changing all the colors of that row to that particular row

            #Changing the rest of the colors of the grid to black (0)
            for i in range(grid.shape[0]):
                for j in range(grid.shape[1]):
                    #If it does not satisfy the condition in the above two loops change the color to black
                    if (i not in storeRow and j != storeCol):
                        grid[i][j] = 0

            print(grid, '\n' ) #Printing output grid for train and test cases

solve()
