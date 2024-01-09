
**Design Choices:**

This algorithm works in a similar way to the autocomplete trie of problem 5.


**Efficiency Analysis:**

The input path has n parts.

In time efficiency, insert and find a handler takes linear time O(n), since there is a complete path traversal in both cases.

For the space complexity, it will be less than the total number of nodes in the trie, which depends on path overlapping for the first parts of the corresponding path. That's the main advantage of using tries.