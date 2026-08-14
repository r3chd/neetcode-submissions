class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for number in nums:
            if number not in result:
                result[number] = 1
            else:
                result[number] += 1
        
        seen = []
        returnList = []

        for i in range(k):
            maximum = 0;
            maxkey = 0;
            for key in result:
                if key not in seen and result[key] > maximum:
                    maximum = result[key]
                    maxkey = key
            
            returnList.append(maxkey)
            seen.append(maxkey)
        
        return returnList
                    