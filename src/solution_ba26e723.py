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
            j = 0
            while( j < grid.shape[1]): #While j is less than the number of columns of the grid
                for i in range(grid.shape[0]):
                    if(grid[i][j] != 0): #If the row is not black (0)
                        grid[i][j] = 6 #Change the color to pink (6)
                j = j + 3 #Repeat the above for every 3rd column as per the challenge                    

            print(grid , '\n') #Printing the output grid for the cases

solve()