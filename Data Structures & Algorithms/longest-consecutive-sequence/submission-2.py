class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0
        for num in numSet:
            longest = 0
            if (num - 1) not in numSet:
                longest += 1
                while (num + longest) in numSet:
                    longest += 1
            if longest > result:
                result = longest
        
        return result