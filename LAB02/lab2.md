Part A — Analysis
Function 1

This function has one loop that runs once for every value from 0 up to number - 1. That means if the input is n, the loop runs n times.

Inside the loop, only simple math operations happen (addition and multiplication). These operations always take the same amount of time no matter how big n is. Because of that, each loop iteration is constant time.

So the total running time grows directly with n.

Time complexity: O(n)

Space complexity: O(1) because only a few variables are used

Function 2

This function does not use any loops. It just calculates a formula using a fixed number of arithmetic operations.

Since the number of operations never changes based on the input size, the running time stays the same no matter how large n gets.

Time complexity: O(1)

Space complexity: O(1)

Function 3

This function uses two nested loops. The outer loop runs about n times. For each pass of the outer loop, the inner loop runs slightly fewer times.

The total number of comparisons ends up being:

n + (n-1) + (n-2) + ... + 1

which is roughly equal to n² / 2.

Because of this, the running time grows proportionally to n². Even if the list is already sorted, the loops still run the same number of times.

Time complexity: O(n²)

Space complexity: O(1) since the list is sorted in place

Function 4

This function runs a loop from 1 to number. That means it executes n times.

Each loop iteration performs a simple multiplication, which is constant time. Since the number of iterations grows directly with n, the running time increases linearly.

Time complexity: O(n)

Space complexity: O(1)


### Timing Data

| Team member | Timing for fibonacci | Timing for sum_to_number |
|-------------|---------------------|-------------------------|
|Japhet       |                     |                         |
