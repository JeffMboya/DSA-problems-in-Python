#Approach #1 (Linear Scan) [Time Limit Exceeded]
#The straight forward way is to brute force it by doing a linear scan.
'''
Complexity analysis

Time complexity : O(n).
Assume that isBadVersion(version)isBadVersion(version) takes constant time to check if a version is bad.
It takes at most n - 1n−1 checks, therefore the overall time complexity is O(n).

Space complexity : O(1).
'''


'''
Approach #2 (Binary Search)
It is not difficult to see that this could be solved using a classic algorithm - Binary search. 
Let us see how the search space could be halved each time below.
'''


def firstBadVersion(self, n: int) -> int:
    i = 1
    j = n
    while (i < j):
        pivot = i + (j - i) // 2
        if (isBadVersion(pivot)):
            j = pivot  # keep track of the leftmost bad version
        else:
            i = pivot + 1  # the one after the rightmost good version

    return i
'''
Complexity analysis
Time complexity : O(log n). The search space is halved each time, so the time complexity is O(log n).
Space complexity : O(1)
'''

'''
Remarks
We use i = 1 instead of 0 as base case because there's no index operation involved and the product version starts from 1.
We use j to keep track of the leftmost bad version we have checked, so that any version after j would not be the first bad version we want.
We use i to keep track of the leftmost unknown version which has a good version before it, so that any version before i would be a good version.
Therefore, i would move towards j step by step and stop when it becomes the first bad version.'''