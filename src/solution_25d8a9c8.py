import sys
import json
import numpy as np


def solve():
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f)

    grid = np.asarray(data['test'][0]['input'])
    for i in range(len(grid)):
        print(grid[i])
    
       


solve()
