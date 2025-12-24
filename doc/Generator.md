# What is a Python Generator?
A Generator in Python is a special type of iterator that allows you to iterate over a potentially large sequence of data *__without__* loading the entire sequence into __memory__ at once.

The key difference between a regular function that returns a list (or other iterable) and a generator function is the use of the __yield__ keyword instead of __return__.

When a generator function is called, it returns a generator object (an __iterator__).

When a value is requested from the generator (e.g., in a for loop or by calling next()), the function executes until it hits a yield statement.

The yield statement __pauses__ the function, __saves__ its local state (variables and instruction pointer), and returns the yielded value.

When the next value is requested, the function resumes exactly where it left off.

This process is called __lazy__ evaluation or __on-demand__ generation.


---
## Generator Expressions (A concise way)
These are similar to list comprehensions but use parentheses __( )__ instead of square brackets __[ ]__.

### Example 2:
 Squares of Numbers A list comprehension creates the entire list in memory:
```Python
# List comprehension (creates list [0, 1, 4, 9] immediately)
my_list = [x*x for x in range(4)]
print(f"List: {my_list}")
```
A generator expression creates a generator object that yields values one at a time:

```Python
# Generator expression (creates generator object)
my_gen_exp = (x*x for x in range(4))
print(f"Generator Expression Object: {my_gen_exp}")

# Iterate over the generator expression
for square in my_gen_exp:
    print(f"Square: {square}")
```


---
## Why Developers Use Generators
Developers primarily use generators for the following use cases:

#### Reading Large Files:
 Processing huge log files or CSVs line by line without loading the entire file content into RAM.

#### Data Science/ML Pipelines: 
Processing massive datasets where samples are fed to a model one batch at a time (e.g., using a generator function as a Keras data sequence).

#### Streaming Data: 
Handling data streams (like network packets, real-time sensor readings) where the total number of items is unknown or potentially infinite.

#### Pipelining/Chain Iterators:
 Creating efficient, readable pipelines where the output of one generator is fed as the input to the next.

 ---

 #### File Tailling using Generator :
  use full for log file as new log record in file 
```python 
import time 

# File Tailling 
def follow(file):
    file.seek(0,2) #go to end of file 
    while (True):
        line = file.readline()
        if not line :
            time.sleep(0.1)
            continue 
        yield line 

```
Open file and tailling it as new line enter it will print line on terminal 

```python
file=open("Generator.md")
of=follow(file=file)
print(type(of))
#itrate over file
for line in of:
    print(line)

    # if line[:1] == '.':
    #  break
```