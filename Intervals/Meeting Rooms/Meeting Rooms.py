"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
"""

def canMeet(intervals):
    intervals.sort(key = lambda i:i[0])
    # print(intervals)
    for i in range(1, len(intervals)):
        prev = intervals[i-1]
        next = intervals[i]

        if prev[1]> next[0]:
            return False
        
    
    return True

print(canMeet([(0,30),(15,20),(5,10)]))

print(canMeet([(5,8),(9,15)]))

