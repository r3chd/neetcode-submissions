class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 0
            else:
                return True
        return False
