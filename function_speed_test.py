import time

# Set the argument for the functions. 
# This value will be passed to each function.
n = 10000000

# Define functions for speed comparison.
def func1(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

def func2(n):
    sum(i ** 2 for i in range(1, n + 1))

def func3(n):
    return n * (n + 1) * (2 * n + 1) // 6

# List of functions to be measured. You can add more functions here, separated by commas.
functions = [func1, func2, func3]
results = []

# A function to measure the execution time of each function. It also outputs the result of the function execution.
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    
    print(f'{func.__name__}:\n{result}\n')
    
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time

# Measure the execution time for each function in the function list
for func in functions:
    elapsed_time = measure_time(func, n) # If there are more arguments, add them separated by commas.
    results.append((elapsed_time, func.__name__))

# Output the results: print the execution time for each function.
for elapsed_time, name in results:
    print(f'{name}: {elapsed_time:.10f}')
