# Part A: Analysis of SortedTable Functions

This section evaluates the time complexity of each member function in the `SortedTable` class with respect to the number of records stored in the table. The analysis focuses on the efficiency and scalability of each operation as the dataset grows.


## 1. insert(key, value)

The `insert` function adds a new key-value pair to the table. It first checks for the existence of the key using the `search` function. If the table has reached its capacity, it resizes the underlying array by creating a new array with double the capacity and copying existing elements. After inserting the new record, the function sorts the table using a nested loop (bubble sort).

Time Complexity: O(n²)  

Explanation:
The function performs a linear search O(n) to check for duplicate keys, followed by a sorting process using bubble sort, which takes O(n²). Since the sorting step dominates the runtime, the overall time complexity is O(n²).


## 2. modify(key, value)

The `modify` function updates the value associated with an existing key by performing a sequential search through the table.

Time Complexity:O(n)  

Explanation:
The function relies on a linear search to locate the specified key. In the worst case, it may need to traverse the entire table.


## 3. remove(key)

The `remove` function deletes a key-value pair from the table. It first locates the target key through a linear search and then shifts subsequent elements to maintain the structure of the table.

Time Complexity: O(n)  

Explanation:
The initial search requires O(n) time, and shifting elements to fill the gap also requires O(n) time. Therefore, the overall time complexity remains O(n).


## 4. search(key)

The `search` function retrieves the value associated with a given key by scanning the table sequentially.

Time Complexity: O(n)  

**Explanation:**  
The function performs a linear search, potentially examining every element until the key is found or the end of the table is reached.


## 5. capacity()

The `capacity` function returns the total number of available slots in the table.

Time Complexity:O(1)  

Explanation: 
This operation simply returns a stored variable and does not depend on the size of the dataset.


## 6. __len__()

The `__len__` function calculates the number of records stored in the table by counting non-None entries.

Time Complexity: O(n)  

Explanation:  
The function iterates through the entire table to count valid elements, resulting in linear time complexity.


## Inefficiencies and Potential Improvements

The current implementation of `SortedTable` contains several inefficiencies that impact performance:

- The `insert` function relies on **bubble sort**, which has a time complexity of O(n²). A more efficient approach would be to insert elements directly into their correct position or use a more efficient sorting or insertion strategy.  
- The `search` function uses **linear search**, despite the table being sorted. This could be optimized using **binary search**, reducing the time complexity to O(log n).  
- The `__len__` function recalculates the number of elements each time it is called. Maintaining a dedicated size variable would allow this operation to run in O(1) time.  
- The resizing process requires copying all elements to a new array, which is costly. However, this operation is acceptable as it occurs infrequently.


## Conclusion

While the `SortedTable` class fulfills its intended functionality, it is not optimized for performance. The reliance on inefficient algorithms such as bubble sort and linear search significantly impacts scalability. By implementing more efficient data handling techniques, such as binary search and maintaining auxiliary variables, the overall performance of the table can be greatly improved, especially when handling larger datasets.