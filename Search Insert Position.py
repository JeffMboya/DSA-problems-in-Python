'''Algorithm

-Initialize the left and right pointers : left = 0, right = n - 1.

-While left <= right:

    Compare middle element of the array nums[pivot] to the target value target.

    If the middle element is the target, i.e. target == nums[pivot]: return pivot.

    If the target is not here:

    If target < nums[pivot], continue to search on the left subarray. right = pivot - 1.

    Else continue to search on the right subarray. left = pivot + 1.

Return left.

'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left

    '''
    Time complexity :O(log N).
    Space complexity :O(1) 
    '''