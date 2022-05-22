
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
"""



def min_meeting_rooms(intervals):
        # Write your code here

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        # print(start)
        # print(end)
        res, count = 0, 0

        s, e = 0, 0
        while s < len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1
            
            else:
                e+=1
                count-=1
            
            res = max(res, count)
        return res


print(min_meeting_rooms(intervals = [(0,30),(5,10),(15,20)]))