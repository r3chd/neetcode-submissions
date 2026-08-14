class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        array = []
        for num, cnt in count.items():
            array.append([cnt, num])
        
        array.sort()

        result = []
        while len(result) < k:
            result.append(array.pop()[1])
        
        return result