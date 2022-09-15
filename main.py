import random
import numpy as np
from matplotlib import pyplot as plt

def bootstrapping(estimate:str, n:int, repeat:int):
    counter = 0
    results = []
    if estimate == 'mean':
        while counter != repeat:
            results.append(np.mean(random.choices(sample,k=n)))
            counter += 1
    elif estimate == 'median':
        pass
    elif estimate == 'var':
        pass
    elif estimate == 'sd':
        pass

    del counter
    return results
    