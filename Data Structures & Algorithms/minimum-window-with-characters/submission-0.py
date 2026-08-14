class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_hash, substring_hash = {}, {}

        for char in t:
            t_hash[char] = 1 + t_hash.get(char, 0)

        have, need = 0, len(t_hash)
        result, length = [-1, 1], float("infinity")

        left = 0
        for right in range(len(s)):
            char = s[right]
            substring_hash[char] = 1 + substring_hash.get(char, 0)

            if char in t_hash and substring_hash[char] == t_hash[char]:
                have += 1
            
            while have == need:
                
                if (right - left + 1) < length:
                    result = [left, right]
                    length = (right - left + 1)
                
                substring_hash[s[left]] -= 1
                if s[left] in t_hash and substring_hash[s[left]] < t_hash[s[left]]:
                    have -= 1

                left += 1
        
        l, r = result

        if length == float("infinity"):
            return ""
        
        return s[l:r+1]