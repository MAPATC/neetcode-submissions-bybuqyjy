class Solution:
    def hasDuplicate(self, nums):
        set1 = set(nums)
        if len(set1) == len(nums):
            return False
        return True