#The naive approach here would be to run through the linked list and create an array of its values, 
# then compare the array to its reverse to find out if it's a palindrome. 
# Though this is easy enough to accomplish, we're challenged to find an approach with 
# a space complexity of only O(1) while maintaining a time complexity of O(N).

#The only way to check for a palindrome in O(1) space would require us to be able to access 
# both nodes for comparison at the same time, rather than storing values for later comparison. 
# This would seem to be a challenge, as the linked list only promotes travel in one direction.
# But what if it didn't?
# The answer is to reverse the back half of the linked list to have the next attribute point 
# to the previous node instead of the next node. 
# (Note: we could instead add a prev attribute as we iterate through the linked list, 
# rather than overwriting next on the back half, but that would technically use O(N) extra space,
# just as if we'd created an external array of node values.)

#The first challenge then becomes finding the middle of the linked list in order to start our 
# reversing process there. For that, we can look to Floyd's Cycle Detection Algorithm.

#With Floyd's, we'll travel through the linked list with two pointers, 
# one of which is moving twice as fast as the other. When the fast pointer reaches the end of the list, the slow pointer must then be in the middle.


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True