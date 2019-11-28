import sys
import json
import numpy as np

def solve(): #Function that contains the logic
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f) #Parsing the JSON file

    var = ['train' , 'test'] 
    #Running for all the training and testing inputs
    for x in var:
        for n in range(len(data[x])):
            grid = np.asarray(data[x][n]['input'])
            for i in range(len(grid)):
                checkVal = grid[i][0] #Storing the first color of the row i.
                check = True #Default value True
                #Checking if the other colors of the row i are equal to checkVal
                for j in grid[i]:
                    if (checkVal!= j):
                        check = False #Check is False if the element is not same
                if (check == True): #For the row containing same colors
                    grid[i] = 5 
                else:
                    grid[i] = 0 #For the rows containing different colors
            print(grid , '\n') #Printing the output grids for all cases.

solve() #Calling the method solve()
