class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # previous solution was O(n^2)
        # this solution is O(n) with O(n) time complexity
        seen = {}
        for i, num in enumerate(nums): 
            complement = target - num
            if complement in seen:
                result = [seen[complement], i]
            else:
                seen[num] = i
        return result