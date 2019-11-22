import sys
import json

try : 
    with open(sys.argv[1] , 'r') as f:
        data = json.load(f)
        print(data)

except:
    print('Please Enter a JSON File Name')