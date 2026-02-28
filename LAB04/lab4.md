# DSA456 – Lab 4

Name: Japheth Igbinovia  
Email: jigbinovia1@myseneca.ca  



What sorting algorithm was the speaker trying to improve?

The speaker was mainly trying to improve QuickSort, specifically the version used inside the C++ standard library (std::sort). He explains that most implementations actually use something called introsort, which starts with QuickSort and switches to HeapSort or Insertion Sort depending on the situation. The talk focuses on how small design decisions inside this hybrid approach can significantly affect real-world performance.

2. At what partition size does Visual Studio switch to a simpler algorithm?

Visual Studio switches to Insertion Sort when the partition size reaches 32 elements. The idea is that QuickSort works well on large partitions, but once the array becomes small enough, Insertion Sort becomes faster because it has lower overhead and works very efficiently on small or nearly sorted data.

3. At what partition size does GNU switch?

GNU switches to Insertion Sort when the partition size reaches 16 elements. It’s interesting that different implementations choose different thresholds. This shows that performance tuning often comes down to experimentation and hardware behavior rather than just theory.

4. Why does switching to binary search not improve insertion sort performance?

Binary search reduces the number of comparisons needed to find the correct insertion point. However, insertion sort spends most of its time shifting elements in memory, not comparing them. Even if you find the position faster, you still have to move the elements. Since memory movement is the expensive part, reducing comparisons does not significantly improve performance. This was one of the surprising insights from the talk.

5. What is branch prediction?

Branch prediction is a technique used by modern CPUs to guess the outcome of conditional statements like if statements. The CPU tries to predict which path the code will take so it can continue executing instructions without waiting. If it guesses correctly, the program runs smoothly. If it guesses wrong, the CPU has to throw away some work and start over, which causes a performance penalty. These penalties can be surprisingly large.

6. What is informational entropy?

Informational entropy measures how much disorder or randomness exists in data. In the context of sorting, entropy represents how much “work” is needed to sort a dataset. The more random the data, the higher the entropy, and the more comparisons are required to organize it. The speaker connects this concept to how sorting algorithms extract order from randomness.

7. What is unguarded insertion sort and why is it faster?

In regular insertion sort, there is a boundary check to make sure the algorithm does not go past the beginning of the array. This check creates an extra conditional branch.

Unguarded insertion sort removes that boundary check. This becomes possible after calling make_heap(), which guarantees that a smallest element exists in a position that prevents out-of-bounds access. Because the boundary check is removed, there are fewer branches, and therefore fewer branch mispredictions. This makes the algorithm faster in practice.

8. What does incorporating conditionals into arithmetic mean?

This means rewriting code so that it avoids if statements and instead uses arithmetic operations or CPU instructions that do not require branching.

For example, instead of using:

if (a < b) swap(a, b);

the algorithm can use conditional move instructions or arithmetic expressions that achieve the same result without creating a branch. This reduces the chance of branch misprediction and improves performance, especially on unpredictable data.

9. Describe the GNU bug.

The speaker describes a situation where GNU’s implementation had an issue related to pivot selection. In certain patterns of input, the pivot choice caused poor partitioning, leading to worse performance than expected. This demonstrates that even widely used library implementations can contain subtle performance problems.

10. What metric is missing?

The missing metric is branch misprediction count.

The graphs in the presentation show that comparisons and moves increased, but overall runtime decreased. This seems contradictory at first. However, the speaker explains that reducing branch mispredictions had a much bigger impact on performance than reducing comparisons. This shows that hardware-level behavior matters just as much as algorithm complexity.

11. What does “fast code is left-leaning” mean?

“Left-leaning” refers to predictable branch behavior. If conditions consistently evaluate in the same direction, the CPU can predict them more accurately. Predictable branching improves performance because it reduces costly pipeline flushes caused by mispredictions.

12. What does “not mixing hot and cold code” mean?

Hot code refers to code that runs frequently. Cold code refers to code that runs rarely, such as error handling.

Mixing hot and cold code together can hurt performance because it reduces instruction cache efficiency. Keeping frequently executed code grouped together improves cache usage and overall speed.


# Part B – Reflection

## 1. What did you find most challenging to understand?

The most challenging part for me was understanding how branch prediction affects performance at the CPU level. I’ve always learned about algorithms in terms of Big-O notation, so I naturally focused on comparisons and theoretical complexity. I never really thought about how the processor executes instructions internally. Learning that a single mispredicted branch can cost dozens of CPU cycles was eye-opening. It made me realize that performance is influenced by hardware behavior just as much as by algorithm design.

## 2. What was the most surprising thing you learned?

The most surprising thing I learned was that increasing comparisons and element moves can sometimes reduce total runtime. At first, this didn’t make sense to me because we’re taught that fewer operations usually mean faster code. However, the speaker showed that reducing branch mispredictions had a much bigger impact on performance than simply reducing comparisons. That completely changed how I think about optimization. It showed me that real-world performance is more complex than theoretical analysis.

## 3. Has this video given you ideas on how you can write better/faster code?

Yes, it definitely has. I now understand that writing fast code is not just about choosing the right algorithm but also about writing predictable and hardware-friendly code. In the future, I will pay more attention to how I use conditionals inside loops, especially in performance-critical sections. I’ll also think more about memory access patterns and predictability instead of only focusing on reducing comparisons. Even if I don’t always need extreme optimization, this video helped me see how much thought goes into writing truly efficient code. 


# References

Alexandrescu, A. (2019). *Sorting Algorithms: Speed Is Found In The Minds of People*. CppCon 2019.  
https://www.youtube.com/watch?v=FJJTYQYB1JQ

Algorithmica. (n.d.). *High-Performance Computing and Branch Prediction*.  
https://en.algorithmica.org/hpc/

Shannon, C. E. (1948). *A Mathematical Theory of Communication*.  
https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

Intel. (n.d.). *Branch Prediction and the Modern Processor*.  
https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html