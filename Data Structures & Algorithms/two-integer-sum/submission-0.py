class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {} # value : index

        for i, j in enumerate(nums):
            diff = target - j # target - value
            if diff in hashMap: # If diff is in the hashMap, we have found the solution
                return [hashMap[diff], i]
            hashMap[j] = i # Update hashMap (j - index, i - value)

        return []