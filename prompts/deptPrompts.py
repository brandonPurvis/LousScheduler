# Dept Level Prompts

from lousScrape import LousList
from lousScrape import Course

ll = LousList()

def strTimeToMinutes(time):
    time = str(time)
    mins = time[-2:]
    hours = time[:-2]
    minutes = int(hours)*60 + int(mins)
    return minutes
    
def getDepartment():
    dept = raw_input("Enter a Department: ")
    return ll.getDeptCourses(dept), dept
    
def averageCourseLength():
    courses, dept = getDepartment()
    sumdiff = sum([ strTimeToMinutes(c.endTime) - strTimeToMinutes(c.startTime) \
                   for c in courses])
    avg = sumdiff / len(courses)
    print("The Average Length of a class in {} is {} minutes".format(dept, avg))

def averageCourseSize():
    courses, dept = getDepartment()
    sumsize = sum([int(c.enrollment) for c in courses])
    avg = sumsize / len(courses)
    print("The Average Size of a class in {} is {} students".format(dept, avg))
