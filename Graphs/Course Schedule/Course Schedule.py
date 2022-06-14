

"""
https://leetcode.com/problems/course-schedule
"""


def canFinish(numCourses, prerequisites):
        
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
          preMap[crs].append(pre)
        
        
        visitSet = set()
        
        def dfs(crs):
          if crs in visitSet:
            return False
          if preMap[crs]==[]:
            return True
          
          visitSet.add(crs)
          
          for pre in preMap[crs]:
            if not dfs(pre) : return False
          
          visitSet.remove(crs)
          preMap[crs] = []
          
          return True
        
        for c in range(numCourses):
          if not dfs(c): return False
        
        return True



print(canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))