import sys
import json
import numpy as np

def solve(): #Function that contains the logic to solve the task
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f) #Parsing the JSON file.

    var = ['train' , 'test']
    #Running for all the training and testing inputs
    for z in var:
        for n in range(len(data[z])):
            grid = np.asarray(data[z][n]['input'])
            count = 0 #Count will contain the number of blue elements
            for x in np.nditer(grid):
                if x!=0 :
                    count = count + 1 #Iterating for every blue element.

            for i in range(len(grid)):
                for x in range(len(grid[i])):
                    #For loop for assigning the red (2) color elements.
                    if ( i == 0 and x < count ):
                        grid[i][x] = 2
                    else:
                        grid[i][x] = 0 
                    if (count > 3):
                        grid[1][1]= 2 # When elements are more than 3 then we place the next element in second row and second column
    
            print(grid , '\n') #Printing the ouput grid
        

solve()