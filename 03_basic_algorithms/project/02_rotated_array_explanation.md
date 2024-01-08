
**Design Choices:**

A modification of binary search was used. If the array is splitted in two halves, the pivot of rotation must be in one of the halves, such that the other half is sorted.

In the sorted part it's possible to check if the target is in that part, otherwise it must be on the other part. Using this information one narrows down the search space.


**Efficiency Analysis:**

The input has n elements, which corresponds to the array length.

The time efficiency will be the one of binary search, namely O(log n), since in each iteration the number of possibilities decreases by a factor of 2, roughly.

For the space efficiency there are no additional data structures, so there is no variation with n, and the efficiency is constant O(1).