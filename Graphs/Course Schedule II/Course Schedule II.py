
"""
https://leetcode.com/problems/course-schedule-ii
"""


def findOrder(numCourses, prerequisites):
        
        
        #build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) }
        
        for crs, pre in prerequisites:
          prereq[crs].append(pre)
          
          
        # a course has 3 possible states
        # visited => crs has been added to output
        # visiting => crs not added to ouput, but added to cycle
        # unvisted => crs not added to output or cycle
        
        output = []
        visit, cycle = set(), set()
        
        def dfs(crs):
          if crs in cycle:
            return False
          if crs in visit:
            return True
          
          cycle.add(crs)
          
          for pre in prereq[crs]:
            if dfs(pre) == False:
              return False
          
          cycle.remove(crs)
          visit.add(crs)
          output.append(crs)
          
        for c in range(numCourses):
          if dfs(c)==False:
            return []
        
        
        return output


print(findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(findOrder(numCourses = 2, prerequisites = [[1,0],[0,1]]))