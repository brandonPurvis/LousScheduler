import urllib2

class Course:
    def __init__(self, data):
        try:
            self.dept = data[0]
            self.courseNumber = data[1]
            self.sectionNumber = data[2]
            self.courseName = data[3]
            self.professor = data[4]
            self.courseType = data[5]        # Lecture / Laboratory
            self.courseHours = data[6]       # ???
            self.monday = data[7]
            self.tuesday = data[8]
            self.wednesday = data[9]
            self.thursday = data[10]
            self.friday = data[11]
            self.startTime = data[12]
            self.endTime = data[13]
            self.location = data[14]
            self.enrollment = data[15]
            self.maxEnrollment = data[16]
            self.latitude = data[17]
            self.longitude = data[18]
        except IndexError:
            raise(IndexError("Failed:" + str(data)))

    def getBuilding(self):
        return self.location

    def getProfessor(self):
        return self.professor

    def getTimes(self):
        return (self.startTime, self.endTime)

    def getDays(self):
        return (self.monday == "true",
                self.tuesday == "true",
                self.wednesday == "true",
                self.thursday == "true",
                self.friday == "true",
                )
    
    def getCourseNumber(self):
        return self.courseNumber

    def getCourseName(self):
        return self.courseName

    def isClassFull(self):
        return self.enrollment >= self.maxEnrollment

    def getCourseType(self):
        return self.courseType

    def __str__(self):
        courseString = "[{:<4} {:<4}] {:<30} {:<15}\n\t[{:<5} - {:>5} |{:<10}]"
        days=["Mo","Tu","We","Th","Fr"]
        courseDays = ""
        for index, day in enumerate(self.getDays()):
            if day:
                courseDays += days[index]
        courseString = courseString.format(self.dept,
                                           self.courseNumber,
                                           self.courseName[:30],
                                           self.courseType[:3],
                                           self.startTime,
                                           self.endTime,
                                           courseDays)
        return courseString

    def conflicts(self, other):
        zipped = zip(self.getDays(), other.getDays())
        merged = map(all,zipped)
        if any(merged):
            lowOne, highOne = map(int,self.getTimes())
            lowTwo, highTwo = map(int,other.getTimes())
            if highTwo in range(lowOne, highOne) or lowTwo in range(lowOne, highOne):
                return True
        return False

        
class LousList():
    BaseUrl = "http://stardock.cs.virginia.edu/louslist/Courses/view/"
    Depts = ["CS", "APMA", "MATH"]

    def splitCourseInfo(self, line):
        data = line.split(";")
        return data

    def getDeptCourses(self, dept):
        courseList = []
        courseWebsite = urllib2.urlopen(LousList.BaseUrl + dept)
        for line in courseWebsite.readlines():
            courseList.append(Course(self.splitCourseInfo(line)))
        return courseList

