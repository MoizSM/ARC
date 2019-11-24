import sys
import json
import numpy as np 


def solve():
    with open(sys.argv[1] , 'r') as f:
        dataset = json.load(f)
        data = np.asarray(dataset["test"][0]["input"])
    for i in range(len(data)):
        if ((i==0) or i == len(data)-1):
            data[i] = 8
        else:
            for j in data[i]:
                data[i][0] = 8
                data[i][-1] = 8
    print(data)

solve()

