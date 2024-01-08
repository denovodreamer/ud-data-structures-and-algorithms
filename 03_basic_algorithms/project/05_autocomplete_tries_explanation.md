
**Design Choices:**

The idea is to build a trie from a given set of words, where a trie is a dynamic set of strings.

After building the trie, it will act as a dictionary. Given a string, it returns the possible suffixes to complete that string, which corresponds to the words starting with that string. Each character in the string corresponds to one node, and in the end it recurses to all possible children nodes.


**Efficiency Analysis:**

The time complexity for the autocompletion feature is O(n), with n the number of characters in the string.

