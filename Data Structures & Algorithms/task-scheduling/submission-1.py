class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit of time
        # minimise idle time

        count = {}
        for c in tasks:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        maxHeap = []
        for c in count:
            maxHeap.append(-count[c])
        
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time