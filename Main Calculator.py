import numpy as np 

def calculate(list):
    if len(list) != 9:
        raise ValueError('List contains 9 decimal values.')
    else: 
        matrix = np.array(list).reshape(3, 3)

    mean = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist())
            (matrix.flatten().var())]
    
    var = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),
           (matrix.flatten().var())]
    
    std = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()),
           (matrix.flatten().max())]
    
    max = [(matrix.max(axis=0).tolist()), (matrix.man(axis=1).tolist()),
           (matrix.flatten().max())]
    
    min = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()),
           (matrix.flatten().min())]
    
    sum = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()),
           (matrix.flatten().sum())]
    
    calculations = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
    }
    return calculations 