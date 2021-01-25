import numpy as np


dt = {}
result = np.loadtxt(
    'aapl.csv',
    usecols= [0,1,-1],
    dtype=['U10','U20','float'], #{'names':['title','date','money'],
           #'formats': ['U10','U20','float']},
    delimiter= ',',
    unpack = False,




)

print(result)
b = result['f0']
print(b)