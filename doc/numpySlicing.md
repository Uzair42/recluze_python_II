# NumPy slicing 
- Uses a
bracket notation, __array[start:stop:step]__ , to select *subsets* of elements along each dimension.

- Indices are zero-based, the start index is **inclusive**, and the stop index is **exclusive**. 

## Basic Slicing Syntax
The general syntax for slicing is arr[start:stop:step]. If any parameter is omitted, defaults are used: 

   - **start**: The index to begin the slice (inclusive). Defaults to 0.
   - **stop**: The index to end the slice (exclusive). Defaults to the    end of the array.
   - **step**: The interval between selected elements. Defaults to 1. 

### 1D Array Examples
Consider a 1D array arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]). 

   - **arr[1:6]** : Elements from index 1 up to (but not including) index 6: [1, 2, 3, 4, 5].

   - **arr[4:]**: Elements from index 4 to the end of the array: [4, 5, 6, 7, 8, 9].

   - **arr[:5]** : Elements from the beginning up to (but not including) index 5: [0, 1, 2, 3, 4].

   -  **arr[::2]** : Every other element in the entire array: [0, 2, 4, 6, 8].

   - **arr[::-1]** : All elements in **reverse** order: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]. 

### Multi-Dimensional Array Examples

For multi-dimensional arrays, you specify slices for each dimension, separated by commas: ***arr[row_slice, column_slice]***
 
 consider 2d array 

```python
import numpy as np
arr_2d = np.array([[1, 2, 3, 4, 5], 
                   [6, 7, 8, 9, 10], 
                   [11, 12, 13, 14, 15]])

```
- **arr_2d[1, 1:4]** : Elements from index 1 to 4 (exclusive) in the second row (index 1): [7, 8, 9].
- **arr_2d[:2, :3]** : First two rows and first three columns (a submatrix):
```
[[1, 2, 3],
 [6, 7, 8]]
```

- **arr_2d[:, 2]** : All rows, but only the third column (index 2): [3, 8, 13]. This returns a 1D array.

- **arr_2d[..., 1]** : The ellipsis (...) represents all preceding dimensions, allowing access to the second element (index 1) of the last dimension for all rows and columns. 

### Key Concepts

   - **Negative Indexing**:
    Negative indices count from the end of the array; e.g., arr[-1] is the last element, and arr[:-1] slices all but the last element.

   - **Views vs. Copies:** Basic slicing generally returns a view of the original array, meaning modifications to the slice will affect the original data. Advanced indexing (using integer arrays or boolean masks) returns a copy.

   - **Modifying Elements:**
    You can assign a value or array of matching shape to a slice to modify the original array in place. 

___
---
---