def simple_generator():
    print("Starting generator...")
    yield 1
    print("Continuing...")
    yield 2
    print("Almost done...")
    yield 3
    print("Finished.")

# 1. Calling the function returns a generator object, the code inside doesn't execute yet
my_gen = simple_generator()
print(f"Generator Object: {my_gen}") # Output will show a generator object

# 2. Iterating/calling next() executes the code up to the yield
print(f"Next value: {next(my_gen)}")
print(f"Next value: {next(my_gen)}")
print(f"Next value: {next(my_gen)}")

# 3. Once all yields are done, calling next() raises StopIteration
# print(next(my_gen)) # This line would raise StopIteration

# The most common way to use it is in a for loop:
for value in simple_generator():
    print(f"Loop Value: {value}")




# List Comprehension Equivalent 
squared_number =[y*y for y in range(6)]
print(f"Comprehension Equivalent : {squared_number}")

import time 

# File Tailling 
def follow(file):
    file.seek(0,2)
    while (True):
        line = file.readline()
        if not line :
            time.sleep(0.1)
            continue 
        yield line 


file=open("Generator.md")

print(follow(file=file))

of=follow(file=file)

print(type(of))

for line in of:
    print(line)
    # if line[:1] == '.':
    #  break