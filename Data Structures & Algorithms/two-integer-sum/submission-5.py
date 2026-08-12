class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, num in enumerate(nums):
            temp = target - num
            if temp in seen:
                res = [seen[temp], i]
            seen[num] = i

        return res
        