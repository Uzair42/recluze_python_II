# Decorator in Python

A **Decorator** is one of Python’s most elegant features.
At its simplest, a decorator is a way to **"wrap"** a function or a method to change or extend its behavior without permanently modifying its original code.

Think of it like adding toppings to a plain cheese pizza. You aren't changing the fundamental pizza (the function); you are just adding extra layers on top of it.

---

## 🛠️ How It Works (The Mechanics)

In Python, functions are **"first-class objects."** This means functions can be passed around as arguments to other functions, just like variables.

A decorator is just a function that takes another function as an input and returns a new function as an output.

### The Anatomy of a Decorator

To understand it, look at this "manual" way of doing it before we use the `@` syntax:

```python
def my_decorator(original_function):
    # This inner function 'wraps' the original one
    def wrapper():
        print("1. Doing something before the function runs.")
        original_function()
        print("2. Doing something after the function runs.")
    
    return wrapper # Return the wrapper, ready to be called

def say_hello():
    print("   Hello!")

# Manual decoration
decorated_hello = my_decorator(say_hello)
decorated_hello()

```

### The "Syntactic Sugar" (`@`)

Python makes this easier with the `@` symbol. Placing `@decorator_name` above a function is the exact same as saying `func = decorator_name(func)`.

```python
@my_decorator
def say_hello():
    print("   Hello!")

say_hello()

```

---

## 🌍 Real-Life Use Cases

Developers use decorators to keep their code **DRY** (Don't Repeat Yourself). Instead of writing the same logic in ten different functions, you write one decorator and apply it to all ten.

### 1. Timing (Profiling)

You want to know how long a specific function takes to run.

```python
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

```

### 2. Authorization (Security)

In web frameworks like Flask or Django, decorators check if a user is logged in before allowing them to see a page.

```python
def login_required(func):
    def wrapper(user_is_logged_in):
        if not user_is_logged_in:
            print("Access Denied: Please log in.")
            return
        return func(user_is_logged_in)
    return wrapper

@login_required
def view_secret_dashboard(user_is_logged_in):
    print("Welcome to the secret dashboard!")

```

---

## 🧠 How to Understand It (The Mental Model)

If you are struggling to wrap your head around it, use these three mental steps:

1. **The Box:** Imagine the decorator is a **box**.
2. **The Gift:** Your original function is a **gift** you put inside that box.
3. **The Delivery:** When someone asks for the "gift," they actually get the **box**. The box might have a bow on top (code before) or a "thank you" note inside (code after), but the gift (the function) is still there in the middle.

### Key Takeaways for Beginners:

* **Nested Functions:** You must be comfortable with functions defined inside other functions.
* **Returning Functions:** Remember that the decorator doesn't *run* the function immediately; it *returns* a new version of it to be run later.
* **`*args` and `**kwargs`:** You will often see these inside decorators so that the decorator can work with any function, regardless of how many arguments that function takes.

---
