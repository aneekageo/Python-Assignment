import time

def time_this(sleeper_func):
    def wrapped_func(sleeptime):
        start_time = time.time()
        sleeper_func(sleeptime)
        print("Total time taken:", time.time() - start_time)
    return wrapped_func

@time_this
def sleeper_func(sleeptime):
    print(f'Sleeping for {sleeptime} seconds')
    time.sleep(sleeptime)
    print('Woke up!')

sleeper_func(2)
