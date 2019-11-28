import sys
import json
import numpy as np 


def solve(): #Logic Funtion
    with open(sys.argv[1] , 'r') as f:
        dataset = json.load(f) #Parsing the JSON file
    
    var = ['train' , 'test']
    #Running for all the training and testing inputs    
    for x in var:
        for n in range(len(dataset[x])):
            gridData = np.asarray(dataset[x][n]['input'])        
            for i in range(len(gridData)):
                if ((i==0) or i == len(gridData)-1):
                    gridData[i] = 8
                else:
                    for _ in gridData[i]:
                        gridData[i][0] = 8
                        gridData[i][-1] = 8
            print(gridData, '\n') #Printing the output gruds

solve()

