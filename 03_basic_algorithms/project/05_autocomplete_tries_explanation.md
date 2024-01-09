
**Design Choices:**

The idea is to build a trie from a given set of words, where a trie is a dynamic set of strings.

After building the trie, it will act as a dictionary. Given a string, it returns the possible suffixes to complete that string, which corresponds to the words starting with that string. Each character in the string corresponds to one node, and in the end it recurses to all possible children nodes.


**Efficiency Analysis:**

The input string to autocomplete has n characters.

Both insert and find a word it takes linear time O(n), since there is a complete string traversal.

For the space complexity, it will be less than the total number of words in the trie, which depends on word overlapping for the beggining of the corresponding strings. That's the main advantage of using tries.
