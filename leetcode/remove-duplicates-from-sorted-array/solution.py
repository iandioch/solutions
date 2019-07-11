class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums) - 1:
            if nums[start] == nums[start+1]:
                del nums[start]
            else:
                start += 1
