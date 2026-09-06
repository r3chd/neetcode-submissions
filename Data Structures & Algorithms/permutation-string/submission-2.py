class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        check = {}
        for char in s1:
            if char not in check:
                check[char] = 1
            else:
                check[char] += 1
        
        left, right = 0, len(s1) - 1

        while right <= len(s2) - 1:
            for i in range(left, right + 1):
                if s2[i] not in count:
                    count[s2[i]] = 1
                else:
                    count[s2[i]] += 1
            if count == check:
                return True
            left += 1
            right += 1
            count = {}
        return False