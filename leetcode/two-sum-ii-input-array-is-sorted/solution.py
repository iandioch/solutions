class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = len(numbers)
        i = 0
        j = c - 1
        while True:
            a = numbers[i] + numbers[j]
            if a == target:
                return [i+1, j+1]
            elif a < target:
                i += 1
            else:
                j -= 1
