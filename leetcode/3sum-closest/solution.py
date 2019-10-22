class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = sum(nums[:3])
        best_diff = abs(target - best)
        nums = sorted(nums)
        prevt = nums[0] - 1
        for targeti in range(len(nums)-2):
            if nums[targeti] == prevt:
                continue
            prevt = nums[targeti]
            l = targeti + 1
            r = len(nums)-1
            while l < r:
                x = nums[targeti] + nums[l] + nums[r]
                d = abs(x - target)
                if d < best_diff:
                    best_diff = d
                    best = x

                if x < target:
                    l += 1
                elif x > target:
                    r -= 1
                else:
                    return target
        return best
