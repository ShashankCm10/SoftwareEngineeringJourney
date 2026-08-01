name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
    result = "PASS"
elif marks >= 75:
    grade = "B"
    result = "PASS"
elif marks >= 60:
    grade = "C"
    result = "PASS"
else:
    grade = "D"
    result = "FAIL"

print("================================")
print("STUDENT GRADE REPORT")
print("================================")
print("Name   :", name)
print("Marks  :", marks)
print("Grade  :", grade)
print("Result :", result)
print("Thank you for using our grading system")