#decorator
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2= time()
        print(f'It took {t2-t1} seconds')
        return result
    return wrapper 


#checking how fast my code runs
@performance
def long_time():
    print('1')
    for i in range (10000000): 
        i*5

@performance
def long_time2():
    print('1')
    for i in list(range(10000000)): 
        i*5

long_time() #   It took 1.6176726818084717 seconds; hence faster
long_time2() #  It took 2.5441975593566895 seconds


# for i in range (10000): 
# took 0.0019948482513427734 seconds

# for i in range (1000000000): 
# took 366.3779978752136 seconds