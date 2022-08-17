#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    new_grade = []

    while len(new_grade) < len(grades):
        for original in grades:
            if original % 5 == 0:
                new_grade.append(original)
            else:

                if (original + 1) % 5 == 0 and original > 37:
                    original_temp = original + 1
                    new_grade.append(original_temp)
                elif (original + 2) % 5 == 0 and original > 37:
                    original_temp = original + 2
                    new_grade.append(original_temp)
                else:
                    new_grade.append(original)

    return new_grade