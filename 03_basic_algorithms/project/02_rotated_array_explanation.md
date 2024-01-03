


The algorithm used was a changed version of a binary search.

After splitting the array in half, one the the halves will be sorted. In the sorted part it's possible to check if the target is in that part, otherwise it must be on the other part.

The time efficiency will be the one of binary search, namely O(log n).