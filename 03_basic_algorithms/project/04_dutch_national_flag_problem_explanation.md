
The algorithm consists in one array traversal and swapping element along the way.

Looping through the array, one keeps track of the last position of the 0 elements and the first position of the 2 elements.

This way, when the current element is 0, one picks the value after the last zero in the current position and puts zero on that position. The algorithm continues with the current position. A similar procedure is used for the 2 elements. Performing this swaps, the elements with 1's stay in the middle of the array.

The time efficieny is O(n) because only one array traversal is performed.