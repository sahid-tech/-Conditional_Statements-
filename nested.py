score = int(input("Enter the student's score (0-100): "))

if score >= 90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 70:
            grade = 'C'
        else:
            if score >= 60:
                grade = 'D'
            else:
                grade = 'F'

print(f"The student's grade is: {grade}")
