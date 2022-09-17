import random
import numpy as np

def bootstrapping(sample, estimate:str, n:int, repeat:int, obs_value = 0):
    counter = 0
    results = []
    above_values = 0
    bellow_values = 0
    if estimate == 'mean':
        while counter != repeat:
            v = np.mean(random.choices(sample,k=n))
            results.append(v)
            counter += 1
            if v >= obs_value:
                above_values += 1
            else:
                bellow_values += 1
    elif estimate == 'median':
        while counter != repeat:
            v = np.median(random.choices(sample,k=n))
            results.append(v)
            counter += 1
            if v >= obs_value:
                above_values += 1
            else:
                bellow_values += 1
    elif estimate == 'var':
        while counter != repeat:
            v = np.var(random.choices(sample,k=n))
            results.append(v)
            counter += 1
            if v >= obs_value:
                above_values += 1
            else:
                bellow_values += 1
    elif estimate == 'std':
        while counter != repeat:
            v = np.std(random.choices(sample,k=n))
            results.append(v)
            counter += 1
            if v >= obs_value:
                above_values += 1
            else:
                bellow_values += 1

    del counter,v
    p_value = above_values/(above_values+bellow_values)
    return (results, p_value)