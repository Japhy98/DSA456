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

Part C – Reflection
How to approach writing recursive functions

When I start writing a recursive function, the first thing I think about is the base case. This is the situation where the function stops calling itself. Without a base case, the function would run forever, so this step is really important.

After that, I figure out how to make the problem smaller so the function can call itself again with a simpler version of the input. I try to think of it as solving one small piece and trusting the function to solve the rest.

Finally, I test edge cases like empty inputs or very small values to make sure the recursion actually stops and returns the correct result.

How analyzing recursive functions differs from non-recursive functions

Analyzing recursive functions feels more mathematical compared to analyzing regular loops. With loops, we usually just count how many times the loop runs. With recursion, we first create a recurrence relation that describes how the function keeps calling itself. Then we expand or “unroll” the recurrence to see the pattern and determine the time complexity.

Even though the methods are different, the goal is the same: count the number of operations and figure out the Big-O complexity. The biggest difference is that recursion focuses on how the problem size gets smaller with each call instead of how many times a loop runs.