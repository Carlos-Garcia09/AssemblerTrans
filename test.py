import re
string = 'ADDD A,PC'
if 'ADDD' in string:
    arr = re.split('[ [,.]', string)[1]
    print(arr)


