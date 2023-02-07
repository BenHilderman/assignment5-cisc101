"""
This program has a tuple of students with their grades, and runs different functions that reference the tuple. 
This includes a print marks function, an average assignment function, an average mark function, a highest mark function, an increase marks function and an add new student function.
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Oct 28, 2022
"""

def printMark(students, studentName):
    """
    Function 1 of assignment 5 - This function prints the grades of a student
    Parameters: students - tuple representing all of the students and their grades, studentName - string representing specific student in the tuple of students
    Return values: None
    """
    for student in students:
        # searching for student with the same name as studentName
        if studentName in student:
            print("The marks for " + str(studentName) + " are:\n    A1: "+str(student[1][0])+"\n    A2: "+str(student[1][1]) + "\n    A3: "+str(student[1][2])+"\n    A4: "+str(student[1][3]))
            return
        else: nameSearch = "lost"
    # if no student matches the same name as studentName
    if nameSearch == "lost":
        print("No student by that name")
    
def averageAssignment(students, assignmentNumber):
    """
    Function 2 of assignment 5 - This function calculates and returns the average mark for the specified assignment.
    It returns -999 if the assignment number isn't 0, 1, 2 or 3
    Parameters: students - tuple representing all of the students and their grades, assignmentNumber - int representing specific assignment number in the tuple of students
    Return values: average mark for specified assignment number - float
    """
    # assignmentNumber must be 0, 1, 2, 3 or 4
    if assignmentNumber == 0 or assignmentNumber == 1 or assignmentNumber == 2 or assignmentNumber == 3:
        sum = 0
        for student in students:
            # adding up the sum of the marks for the specified assignment
            sum += (student[1][assignmentNumber])
        # returning the average mark for the specified assignment
        return (sum/(len(students)))
    else: return -999

def averageMark(students, studentName):
    """
    Function 3 of assignment 5 - This function calculates and returns the average mark for the specified student.
    It returns 0 if the student name isn't in the students tuple
    Parameters: students - tuple representing all of the students and their grades, studentName - string representing the student name
    Return values: average mark for specified student - float
    """
    for student in students:
        # searching for student with the same name as studentName
        if studentName in student:
            # returning the average mark of the specified student
            return(((student[1][0]) + (student[1][1]) + (student[1][2]) + (student[1][3]))/4)
        else: nameSearch = "no"
    # if no student matches the same name as studentName
    if nameSearch == "no":
        return 0

def highestAverageMark(students):
    """
    Function 4 of assignment 5 - This function returns the highest average mark(s).
    Parameters: students - tuple representing all of the students and their grades
    Return values: highest average mark(s) - float or list if theres 2 or more highest marks
    """
    highestAverageMarkOfStudent = 0
    for student in students:
        # gets mark of student the loop is currently on
        averageMarkOfStudent = averageMark(students, student[1])
        # compares current student's mark with highest mark to see if its higher
        if averageMarkOfStudent > highestAverageMarkOfStudent:
            highestAverageMarkOfStudent = averageMarkOfStudent
            finalHighestStudent = student[0]
        # compares current student's mark with highest mark to see if its the same
        elif averageMarkOfStudent == highestAverageMarkOfStudent:
            finalHighestStudent = (finalHighestStudent) + ", " + (student[0])
    finalHighestStudent = [finalHighestStudent]
    return finalHighestStudent

def increaseMarks(students):
    """
    Function 5 of assignment 5 - This function increases every mark by 1
    Parameters: students - tuple representing all of the students and their grades
    Return values: None
    """
    for student in students:
        # raising every mark by 1

        # mark cannot go higher than 100
        if student[1][0] != 100:
            student[1][0] = student[1][0] + 1
        if student[1][1] != 100:
            student[1][1] = student[1][1] + 1
        if student[1][2] != 100:
            student[1][2] = student[1][2] + 1
        if student[1][3] != 100:
            student[1][3] = student[1][3] + 1

def addNewStudent(students):
    """
    Function 6 of assignment 5 - This function adds a new student using the user's inputs for the name and four different grades
    Does not allow a repeat name
    Parameters: students - tuple representing all of the students and their grades
    Return values: an updated tuple of the students that includes the new student - tuple
    """
    repeat = "yes"
    while repeat == "yes":
        repeat = "no"
        # user inputs the name of the student
        studentName = input("Enter the name of the student (Cannot be a repeat name):")
        for student in students:
            # repeating while loop if the student name entered is the same as one in the students tuple
            if studentName == student[0]:
                repeat = "yes"

    # user inputs the first mark of the new student
    repeat1 = "yes"
    while repeat1 == "yes":
        repeat1 = "no"
        firstMark = int(input("Enter the first mark (Cannot be bigger than 100 or less than 0):"))
        if firstMark > 100 or firstMark < 0:
            repeat1 = "yes"
    # user inputs the second mark of the new student
    repeat2 = "yes"
    while repeat2 == "yes":
        repeat2 = "no"
        secondMark = int(input("Enter the second mark (Cannot be bigger than 100 or less than 0):"))
        if secondMark > 100 or secondMark < 0:
            repeat2 = "yes"
    # user inputs the third mark of the new student
    repeat3 = "yes"
    while repeat3 == "yes":
        repeat3 = "no"
        thirdMark = int(input("Enter the third mark (Cannot be bigger than 100 or less than 0):"))
        if thirdMark > 100 or thirdMark < 0:
            repeat3 = "yes"
    # user inputs the fourth mark of the new student
    repeat4 = "yes"
    while repeat4 == "yes":
        repeat4 = "no"
        fourthMark = int(input("Enter the fourth mark (Cannot be bigger than 100 or less than 0):"))
        if fourthMark > 100 or fourthMark < 0:
            repeat4 = "yes"
    newStudents = []
    for student in students:
        # recreating students tuple as a list so I can add the new student to the list
        newStudents += student
    newStudent = (studentName, [firstMark, secondMark, thirdMark, fourthMark])
    newStudent = [(newStudent)]
    newStudents = students + newStudent
    return newStudents

def main():
    #leave the next 3 lines in your code.
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    print("Here is the data set", students)
    print("This program doesn't do anything yet.  Complete the program as per the comments ")

    # calling printMark() with "Xinrong" as the name
    print("Using the printMark function to print Xinrong's marks:")
    printMark(students, "Xinrong")
    # calling printMark() with "Sima" as the name
    print("Using the printMark function to print Sima's marks:")
    printMark(students, "Sima")
    # calling printMark() with my name (Benjamin) who isn't a student
    print("Using the printMark function for Benjamin who is not a student:")
    printMark(students, "Benjamin")

    # calling averageAssignment() for the first mark of each student
    print("Using the averageFirstAssignment function to get the average mark for assignment 1:")
    averageFirstAssignment = (averageAssignment(students, 0))
    # printing the average mark for the first mark of each student
    print(averageFirstAssignment)

    # calling averageMark to get Jane's overall average
    print("Using the averageMark function to print Jane's overall average:")
    print(averageMark(students, "Jane"))
    # calling averageMark for Benjamin who is a student that doesn't exist
    print("Using the averageMark function with a student who doesn't exist:")
    print(averageMark(students, "Benjamin"))

    # printing the name(s) of the student(s) with the highest average mark(s)
    print("Using the highestAverageMark function to print the student(s) with the highest average mark(s):")
    print(highestAverageMark(students))

    # calling addNewStudent to let the user add a new student
    print("Using the addNewStudent function to add a new student:")
    students = addNewStudent(students)

    #leave this in your code so that we can see the new student list.
    print(students)
    
    #increase the marks 
    print("Using the increaseMarks function to increase every mark by 1 (cannot go above 100):")
    increaseMarks(students)

    #leave this so that we can see the change in the marks.
    print(students)

main() 