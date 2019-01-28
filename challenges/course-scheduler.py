"""
#92
Airbnb

We're given a hashmap with a key courseId and value a list of courseIds, which represents that the prerequsite of courseId is courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

"""

courseMap = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}

completedCourses = []

def addToCompletedCourses(course):
    if course not in completedCourses:
        # print("Completed:", course)
        completedCourses.append(course)

def completeCourse(course, currentPrerequisites):
    # Cyclic Dependency
    if course in currentPrerequisites:
        return False
    
    # Cannot take up this course
    if course not in courseMap.keys():
        return False
    # No prerequisites for this course
    elif courseMap[course] == []:
        addToCompletedCourses(course)
        return True
    
    for prerequsite in courseMap[course]:
        if prerequsite not in completedCourses:
            canComplete = completeCourse(prerequsite, currentPrerequisites+[course])
            if canComplete == True:
                pass
            else:
                return False
    
    addToCompletedCourses(course)
    return True


def findCourseSchedule(courseMap):
    # Check if every course can be completed
    for course in courseMap.keys():
        if completeCourse(course, []) == False:
            return None
    return completedCourses


def main():
    print(findCourseSchedule(courseMap))

if __name__ == "__main__":
    main()
