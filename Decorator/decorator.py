
def logger(func):
    print("its inside logger Funcitons")

    def wrapper(n):
        print("inside the wrapper Funciton")
        v=func(n)
        print("Wrapper Going To return Reseult v=",v)
        return v
    
    print("logger going to return its value which is function =",wrapper)
    return wrapper


counter=0
@logger
#Syntactic Sugar for logger(fib) decorator which is samwe as logged_fib=logger(fib)
def fib(n):
    global counter
    counter += 1
    print(f"fib called with n={n}, call count={counter}")
    if n <= 1 :
        return n
    else:
        return fib(n-2) + fib(n-1)
    


#Calling 

# print(fib(8))


# logged_fib=logger(fib)

# Logger(fib) Return wrapper funciton to logged_fib funciton
# and let call the logged_fib() is which points to wrapper inside the logger

# logged_fib(50)

# print(fib(900))  # Normal Call without logger decorator

# @logger
# def fib_decorated(n):
#     if n <= 1 :
#         return n
#     else:
#         return fib_decorated(n-2) + fib_decorated(n-1)  
    
# fib_decorated=fib_decorated(5)
# print("Decorated Fib Function =",fib_decorated)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation():
    time.sleep(1.5) # Simulating work
    return "Done!"

heavy_computation()


