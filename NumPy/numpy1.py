#%%
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,40)
print(x)
type_x=type(x)
print(type_x)

y = np.cos(x)
print(y)

s=np.sin(x)

plt.figure() #create a new figure window 
plt.plot(x, y, marker='s', label='Cosine')
plt.plot(x,s,marker='x', label='Sine')
plt.legend() #showing legend in as per label defined in plot function
plt.xlabel('X-axis')
plt.ylabel('cos / sin  Value')
plt.title('cos and sin Function Plot')
plt.grid(True)
plt.show()

#%% [markdown] 
# # Array Creation  

a = np.array([1, 2, 3])  # Create a 1D array
print("1D Array:", a)

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2D array
print("2D Array:\n", b)

c = np.zeros((2, 3))  # Create a 2D array of zeros
print("2D Array of Zeros:\n", c)

d = np.ones((3, 2))  # Create a 2D array of
print("2D Array of Ones:\n", d)

e = np.eye(3)  # Create a 3x3 identity matrix
print("3x3 Identity Matrix:\n", e)

#%% [markdown]
# # Array Operations

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("Array x:", x)
print("Array y:", y)

# Element-wise addition
add = x + y
print("Element-wise Addition:", add)

# Element-wise multiplication
mul = x * y
print("Element-wise Multiplication:", mul)

# Dot product
dot = np.dot(x, y)
print("Dot Product:", dot)
#%% [markdown]
# # Statistical Functions

data = np.array([1, 2, 3, 4, 5])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
#%% [markdown]
# # Reshaping Arrays    

arr = np.arange(12)  # Create a 1D array with values from 0 to 11
print("Original Array:", arr)

reshaped_arr = arr.reshape((3, 4))  # Reshape to 3 rows and 4 columns
print("Reshaped Array (3x4):\n", reshaped_arr)

#%% [markdown]
# # Indexing and Slicing

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# Indexing
print("Element at index 2:", arr[2])
# Slicing
print("Elements from index 1 to 3:", arr[1:4])
#%% [markdown]
## Boadcasting
#  mean is that numpy will automatically expand 
# the smaller array to match the shape of the larger array 
# during arithmetic operations.


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])

print("Array A:\n", A)
print("Array B:", B)

# it calculates as follows:
# First Row: [1+10, 2+20, 3+30] = [11, 22, 33]
# Second Row: [4+10, 5+20, 6+30] = [14, 25, 36] 


# Broadcasting
C = A + B
print("Result of Broadcasting (A + B):\n", C)   

#%% [markdown]
# # Saving and Loading Arrays

arr = np.array([1, 2, 3, 4, 5])

np.save('array.npy', arr)  # Save array to a .npy file

loaded_arr = np.load('array.npy')  # Load array from the .npy file

print("Loaded Array:", loaded_arr)

# %% [markdown]
# # Linear Algebra with NumPy

#%% Linear Algebra Operations

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

## linear Algebra operation 

# Matrix Multiplication
mat_mult = np.dot(A, B)
print("Matrix Multiplication (A . B):\n", mat_mult)
#%%[markdown]
# # Matrix Inversion
A_inv = np .linalg.inv(A)
# inverse of matrix A is calculated using the formula:
# 1/(ad-bc) * [[d, -b], [-c, a]]

# steps:
# 1. Calculate the determinant (ad - bc)
# 2. Swap the elements a and d.
# 3. Change the signs of b and c.   


# where A = [[a, b], [c, d]]
print("Inverse of Matrix A:\n", A_inv)

#%% [markdown]  
# # Eigenvalues and Eigenvectors
# The eigenvalues and eigenvectors of a matrix A are calculated by solving the characteristic equation:
# det(A - λI) = 0
# where λ represents the eigenvalues and I is the identity matrix.  
A = np.array([[4, -2], [1, 1]])


eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)



