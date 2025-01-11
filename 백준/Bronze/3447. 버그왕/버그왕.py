import sys 
import re
code=sys.stdin.readlines()
for i in code:     
    while True:
        result=re.sub('BUG','',i)         
        if 'BUG' in result: i= result
        else: 
            print(result,end="") 
            break