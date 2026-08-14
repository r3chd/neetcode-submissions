class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # so here, for each num in nums, we just check their chars count
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # array here is for, we put into an array the count and the number
        array = []
        for num, cnt in count.items():
            array.append([cnt, num])
        
        # sort this array so that the smallest number is first if count is equal
        array.sort()

        # our resulti s just the k best
        result = []
        while len(result) < k:
            result.append(array.pop()[1])
        
        # return this result
        return result