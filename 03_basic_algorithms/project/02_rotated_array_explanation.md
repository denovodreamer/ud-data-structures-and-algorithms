

A modification of binary search was used. If the array is splitted in two halves, the pivot of rotation must be in one of the halves, such that the other half is sorted.

In the sorted part it's possible to check if the target is in that part, otherwise it must be on the other part. Using the information one narrow down the search space.

The time efficiency will be the one of binary search, namely O(log n).