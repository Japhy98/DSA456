# Lab 3 – Recursive Functions Analysis

### Function 1

**Basic operation:** multiplication

Each recursive call performs one multiplication.

Base cases:
T(0) = 1  
T(1) = 1  

Recurrence relation:
T(n) = T(n-1) + 1

Unrolling the recurrence:
T(n) = T(n-1) + 1  
     = T(n-2) + 2  
     = T(n-3) + 3  
     ...  
     = T(1) + (n-1)  
     = n  

**Time Complexity:** O(n)

### Function 2

function2 simply calls recursive_function2 once, so its cost is constant.

Let R(n) be the cost of recursive_function2 where n is the string length.

Each recursive call compares two characters and reduces the problem size by 2.

Recurrence relation:
R(n) = R(n-2) + 1  
Base case: R(0) = 1 or R(1) = 1

Unrolling:
R(n) = R(n-2) + 1  
     = R(n-4) + 2  
     = R(n-6) + 3  
     ...  
     = R(0) + n/2  

**Time Complexity:** O(n)

### Function 3 

Each recursive call cuts the problem size in half.

Recurrence relation:
T(n) = T(n/2) + 1

Unrolling:
T(n) = T(n/2) + 1  
     = T(n/4) + 2  
     = T(n/8) + 3  
     ...  
     = T(1) + log₂(n)

**Time Complexity:** O(log n)
