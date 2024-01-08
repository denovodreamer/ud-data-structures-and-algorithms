
**Design Choices:**

A modified version of binary search was used. The square root of the target must be between zero and the target.

The search is performed splitting every time this range in half and check if the square of the middle element is less or greater than the target.

The square root is found when the square of the middle element is equal to the floor of the target squared root.


**Efficency Analysis:**

The input has n elements, which corresponds to the array length.

Time efficiency is of O(log n) . This is the same as binary search, since in each iteration the number of possibilities decreases by a factor of 2, roughly.

For the space efficiency there are no additional data structures, so there is no variation with n, and the efficiency is constant O(1).