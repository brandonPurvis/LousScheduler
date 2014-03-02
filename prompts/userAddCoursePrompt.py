# addCourse
from lousScrape import LousList
from lousScrape import Course

def searchCourses(courses):
    print ("Search By Name: ")
    searchTerm = raw_input(": ")
    matches = [course for course in courses if -1 != course.getCourseName().lower().find(searchTerm.lower())]
    if matches:
        return matches
    else:
        print("Yields No Results")
        return courses

def narrowCriteria(courses):
##    print("Select Criteria")
##    print("1 - Course Number")
    raise NotImplementedError

def displayCourses(courses, selectedCourses):
    print("____________COURSES____________")
    courseString = ""
    for index, course in enumerate(courses):
        conflicts = any([sc.conflicts(course) for sc in selectedCourses])
        
        conflictStr ="[ *(C)* ]" if conflicts else " "
        courseString += "{:>5}{:>9}: {:>20}".format(index, conflictStr, str(course))
        print(courseString)
    
def userAddCoursePrompt(deptCourses = [], selectedCourses = []):
    louslist = LousList()
    if not deptCourses:
        department = raw_input("COURSE DEPT ACRONYNM (ex APMA): ")
        deptCourses = louslist.getDeptCourses(department)
        
    selectedCourse = selectedCourses
    
    print("{} Courses Found".format(len(deptCourses)))
    print("-------------------")
    print("1 - Search Courses ")
    print("2 - Narrow Criteria")
    print("3 - Display Courses")
    print("4 - Select Course  ")
    print("x -      Exit      ")
    print("-------------------")
    resp = raw_input(": ")

    if resp == "x" or resp == "X":
        return None
    
    elif resp == "1":
        # Search
        deptCourses = searchCourses(deptCourses)
            
    elif resp == "2":
        # Narrow
        deptCourses = narrowCriteria(deptCourses)

    elif resp == "3":
        # Display
        displayCourses(deptCourses, selectedCourses)
        
    elif resp == "4":
        # Select
        displayCourses(deptCourses, selectedCourses)
        selectedIndex = raw_input("Course Number: ")
        if (selectedIndex.isdigit() and selectedIndex < len(deptCourses)):
            selectedCourse = deptCourses[int(selectedIndex)]
    else:
        print("Invalid Entry")

    if resp != "4":
         return userAddCoursePrompt(deptCourses, selectedCourses)
    else:
        return selectedCourse
