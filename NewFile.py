print("Hello world")

import pandas as pd
ser1 = pd.Series([1,2,3])
print(ser1)

from MyModule import Animal
lion = Animal("Bob")
print(lion.name)

from joblib import Parallel, delayed
import multiprocessing
import time

def myfunction(i):
    time.sleep(2)
    print(i)
    return i

if __name__ == '__main__': #this is Windows-specific
    #start=time.time()
    #for i in range(10):
    #    myfunction(i)
    #print("SERIAL",time.time() - start)

    start=time.time()
    num_cores = multiprocessing.cpu_count()
    print("Number of cores used:" + str(num_cores))
    results = Parallel(n_jobs=num_cores)(delayed(myfunction)(i) for i in range(10))
    #parallel takes two arguments: how many times you want to split and what you want to split
    print("PARALLEL",time.time()-start)
    print(results)
