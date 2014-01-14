# UserInterface
import os
import sys
import pickle
from prompts import *
##from addCourse import displayCourses
##from addCourse import userAddCoursePrompt

def bugReport(error):
    from datetime import datetime
    import textwrap
    
    print("You have founda bug!")
    print("Explain what you did to produce the bug: ")
    userReport = raw_input(": ")
    curDateTime = datetime.now().strftime("%b %m %y at %H:%M")

    report = textwrap.fill("\n<[{d}]{r}>\n{e}\n".format(r=userReport,
                                                        d=curDateTime,
                                                        e=str(sys.exc_info()[0])),
                                                        62,
                                                        break_long_words = False)

    reportFile = open("bugReport.txt", "a")
    try:
        reportFile.write(report)
        raise error
    finally:
        reportFile.close()
                
def checkForConflicts(courses):
    """Check the course list for scheduling conflicts """

    conflicts = []
    tested = []
    for courseOne in courses:
        safe = True
        for courseTwo in courses:
            if courseOne and courseTwo and courseOne != courseTwo and courseTwo not in tested:
                if courseOne.conflicts(courseTwo):
                    conflicts.append((courseOne,courseTwo))
                    safe = False
        tested.append(courseOne)            
    print("CONFLICTS:")

    if not conflicts:
        print("NONE")
    for conflict in conflicts:
        c1, c2 = conflict
        print("{}\n{}\n".format(str(c1),str(c2)))
    return conflicts
            
def displayCalendar(courses):
    """Display the cources in a schedule like format"""

    week = {"monday"    :[],
            "tuesday"   :[],
            "wednesday" :[],
            "thursday"  :[],
            "friday"    :[],
            }
    dayNames = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    for course in courses:
        if course:
            days = monday, tuesday, wednesday, thursday, friday = course.getDays()
            
            if monday:
                week["monday"].append(course)
            if tuesday:
                week["tuesday"].append(course)
            if wednesday:
                week["wednesday"].append(course)
            if thursday:
                week["thursday"].append(course)
            if friday:
                week["friday"].append(course)

    for day in dayNames:
        courses = week[day]
        courses.sort(key = lambda x: int(x.getTimes()[0]))
        
        print("--------{}---------".format(day))
        for course in courses:
            print(str(course))
            print("{}  {}".format(course.getProfessor(), course.getBuilding()))
            print 
class App:
    def __init__(self):
        self.courses = []
        self.running = True

    def showMainOptions(self):
        print("             UVA               ")
        print("-----Lous-Schedule-Maker-------")
        print("1 -      Add Courses           ")
        print("2 -     Remove Course          ")
        print("3 -     Save Courses           ")
        print("4 -    Display Courses         ")
        print("5 -      Conflicts?            ")
        print("6 -     Load Schedule          ")
        print("7 -     Calendar View          ")
        print("8 -    Replace Course          ")
        print("x -      Exit Course           ")
        resp = raw_input(": ")
        
        try:
            if resp == "x" or resp == "X":
                self.userExitProgram()

            elif resp == "1":
                # Add
                course = self.userAddCourse()
                if course:  self.courses.append(course)

            elif resp == "2":
                # Remove
                courses = self.userRemoveCourse()
                if courses:
                    self.courses = courses
            elif resp == "3":
                # Save
                self.userSaveCourses()

            elif resp == "4":
                # Display
                self.userDisplayCourses()

            elif resp == "5":
                # Conlficts
                self.checkForConflicts()

            elif resp == "6":
                # Load
                self.userLoadCourses()

            elif resp == "7":
                # Calendar View
                self.displayCalendar()

            elif resp == "8":
                # Replace Course
                self.replaceCourse()

            else:
                self.invalid(resp)
        except NotImplementedError:
            print("*_* Feature Not Implemented In This Version *_*")

        except Exception as e:
            bugReport(e)

        if self.running:
            self.showMainOptions()

    def userAddCourse(self):
        course = userAddCoursePrompt(selectedCourses = self.courses)
        self.courses.append(course)

    def userRemoveCourse(self):
        userRemoveCoursePrompt(self.courses)

    def userSaveCourses(self):
        userSaveCoursePrompt(self.courses)

    def userDisplayCourses(self):
        displayCourses(self.courses, [])

    def userLoadCourses(self):
        loadedCourses = userLoadCoursesPrompt()
        if loadedCourses:
            self.courses = loadedCourses
            
    def checkForConflicts(self):
        checkForConflicts(self.courses)

    def replaceCourse(self):
        userReplaceCoursePrompt(self.courses)        

    def displayCalendar(self):
        displayCalendar(self.courses)

    def invalid(self, response):
        print("{} is not a valid entry.".format(response))

    def userExitProgram(self):
        print("Would you like to save your schedual?")
        resp = raw_input(": ")
        if resp[0] == "y" or resp[0]=="Y":
            self.userSaveCourses()
        print("Exiting Application")
        print("ENTER TO TERMINATE WINDOW")
        raw_input()
        self.running = False

if __name__ == "__main__":
    lousScheduleMakerApp = App()
    lousScheduleMakerApp.showMainOptions()
