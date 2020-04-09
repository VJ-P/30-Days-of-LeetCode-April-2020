# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

# Examples:
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.

def countElements(arr):
    # Create a set to keep track of all the elements in the array
    fc = set() # frequency counter
    ans = 0
    # Pass thorugh the arr once and add all of the elements of the array into the map
    for i in arr:
        if not(i in fc):
            fc.add(i)
    # Pass through a second time to check if the x+1 element is in the array
    for i in arr:
        if (i+1 in fc):
            ans += 1
    return ans