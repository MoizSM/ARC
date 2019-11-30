import sys
import json
import numpy as np 


def solve(): #Logic Funtion
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f) #Parsing the JSON file
