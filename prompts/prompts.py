
def userReplaceCoursePrompt(courses):
    raise NotImplementedError

def userRemoveCoursePrompt(courses):
    """Prompt the user to remove a course

    Returns the list of courses with the
    cources removed
    """
    
    displayCourses(courses, [])
    print("x - Exit")
    resp = raw_input("Remove Course: ")
    
    if resp != "x" and resp != "X":
        courses.remove(courses[int(resp)])
    return courses

def userSaveCoursePrompt(courses):
    """Prompt the user to save their course list.
    """

    filename = raw_input("File Name: ")
    if not (filename == "x" or filename == "X"):
        writeTo = open(filename + ".txt", "w")
        pickleSave = open(filename + ".pickle","w")
        try:
            writeTo.write(filename)
            writeTo.writelines(map(str, courses))
            pickle.dump(courses, pickleSave)
        finally:
            writeTo.close()
            pickleSave.close()

def userLoadCoursesPrompt():
    """Promt the user to save their account """

    options = []
    for filename in os.listdir(os.curdir):
        if filename[-7:] == ".pickle":
            options.append(filename)
    print "______Saved Files________"
    for index, option in enumerate(options):
        print("{:<3} - {:<10}".format(index, option))
    resp = raw_input("File Number: ")
    if resp == "x" or resp == "X":
        return None

    elif int(resp) in range(len(options)):
        try:
            loadFile = open(options[int(resp)], "r")
            return pickle.load(loadFile)
        finally:
            loadFile.close()

    else:
        print("invalid response")
        return None    
            
