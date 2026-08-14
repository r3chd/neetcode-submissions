class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []
        
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            req_course = prerequisites[i][1]
            prereq[course].append(req_course)
        
        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return output

            