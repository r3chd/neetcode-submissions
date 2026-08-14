class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums): 
            x = target - num
            if x in seen:
                result = [seen[x], i]
                return result
            else:
                seen[num] = i
        
        return []