import math

def decimals(val):
    e = round(math.e, val)
    str_e = str(e)
    n_list = list(str_e)
    return e

roundTo = input('Enter the number of digits you want after the e: ')

try:
    rountInt = int(roundTo)
    print(decimals(rountInt))
except:
    print('you did not enter an integer')
