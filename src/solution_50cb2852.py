import numpy as np
import sys
import json

def solve():
    with open(sys.argv[1] , 'r') as f:
        dataset = json.load(f)
        data = np.asarray(dataset["test"][0]["input"])
    newArray = np.zeros(np.shape(data))
    # print(newArray)
    for i in np.unique(data):
        dataCopy = np.where(data == i, i , 0)
        if(dataCopy.any() != 0):
            pos = []
            # print(dataCopy , '\n')
            for x in range(len(dataCopy)):
                for y in range(len(dataCopy[x])):
                    if (dataCopy[x][y] == i):
                        pos.append([x,y])
    
    print(newArray, '\n')

solve()