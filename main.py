
name = input("Enter your name: ")
course = int(input("Enter your course: "))
grade = float(input("Enter your grade: "))

information = {"Name: ":name
               , "Course":course
               , "Grade":grade}



if grade >= 99:
    print(information)
    print("With Highest Honor")
elif grade >= 95:
    print(information)
    print("With Higher Honor")
elif grade >= 90:
    print(information)
    print("With High Honor")
elif grade >= 80:
    print(information)
    print("Passed")
else:
    print(information)
    print("Failed")

