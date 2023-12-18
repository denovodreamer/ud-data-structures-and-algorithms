
Since the active directory resembles a tree structure, the bread first search was used.

It was chosen BFS instead of a DFS, because users tend to be in upper groups, to have more access to directories.

For the efficiency, the worst case is searching the all set of users and groups, which is O(n).