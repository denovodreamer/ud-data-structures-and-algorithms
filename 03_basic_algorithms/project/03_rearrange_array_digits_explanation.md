
**Design Choices:**

For an array with integer digits, the number resulting from the combination of the digits is larger if the largest digits come in the begging. This can be accomplished by a sorting algorithm such as Quick Sort.

Since the aim is to split the array into two number that maximize the sum, this can be achived if one sorts the array in decresing order, and extracts two numbers from odd and even positions.


**Efficiency Analysis:**

The input has n elements, which corresponds to the array length.

For the time efficiency, the Quick Sort takes O(n log n), and the extraction of the two numbers takes linear time from the one time traversal of the array. The resulting time complexity is then O(n log n).