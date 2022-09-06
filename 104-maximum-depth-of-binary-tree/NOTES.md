Here the Time Complexity is O(N); in every case we are visiting every node.
​
The Space Complexity is also O(N). In the worst case, we are dealing with a skewed tree. Therefore the recursion stack will be of size O(N) because we never unravel it until we hit our base case (which is being a leaf node here).