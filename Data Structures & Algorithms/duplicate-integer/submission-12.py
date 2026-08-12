class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n] = 0
            else:
                return True
        return False