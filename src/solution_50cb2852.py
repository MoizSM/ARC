import numpy as np
import sys
import json

def solve():
    with open(sys.argv[1] , 'r') as f:
        dataset = json.load(f)
        data = np.asarray(dataset["test"][0]["input"])
    
    for i in range(len(data)):
        print(data[i] , '\n\n')

solve()