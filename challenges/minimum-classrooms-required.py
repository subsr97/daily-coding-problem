"""
#21
Snapchat

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""

def findMaximumClassroomsRequired(timeIntervals):
    eventList = []

    for (start, end) in timeIntervals:
        eventList.append((start, "start"))
        eventList.append((end, "end"))
    
    eventList.sort()

    classroomsRequired = 0
    maxClassroomsRequired = 0
    
    for (time, event) in eventList:
        if event == "start":
            classroomsRequired += 1
        elif event == "end":
            classroomsRequired -= 1
        if classroomsRequired > maxClassroomsRequired:
            maxClassroomsRequired = classroomsRequired
    
    return maxClassroomsRequired

if __name__ == "__main__":
    timeIntervals = [(30, 75), (0, 50), (60, 150)]
    print(findMaximumClassroomsRequired(timeIntervals))