class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prevt = 1
        nums = sorted(nums)
        for targeti in range(len(nums)-2):
            if nums[targeti] > 0:
                break
            if nums[targeti] == prevt:
                continue
            prevt = nums[targeti]
            l = targeti + 1
            r = len(nums)-1
            while l < r:
                x = nums[targeti] + nums[l] + nums[r]
                if x < 0:
                    l += 1
                elif x > 0:
                    r -= 1
                else:
                    ans.append((nums[targeti], nums[l], nums[r]))
                    prevl = nums[l]
                    while l < r + 1 and nums[l] == prevl:
                        l += 1
                    if l == r:
                        break
        return ans
