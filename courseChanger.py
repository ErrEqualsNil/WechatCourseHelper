path = "./classes.json"
import JsonChange

def AddCourse(courseName,weekStr,Day,Time,Place,Teacher):
    weeks = eval(weekStr)
    newCourseDict = {}
    newCourseDict['Week'] = weeks
    newCourseDict['Day'] = Day
    newCourseDict['Time'] = Time
    newCourseDict['Place'] = Place
    newCourseDict['Teacher'] = Teacher
    dict = JsonChange.read(path)
    if courseName in dict.keys():
        dict[courseName].append(newCourseDict)
    else:
        dict[courseName] = [newCourseDict]

    JsonChange.change(path,dict)
    return "Success"

def deleteCourse(CourseName):
    dict = JsonChange.read(path)
    if CourseName in dict.keys():
        dict.pop(CourseName)
        JsonChange.change(path,dict)
        return "Success"
    else:
        return "Fail"
