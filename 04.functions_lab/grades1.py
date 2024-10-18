def corresponding_grade(current_grade):
    if 2.00 <= current_grade <= 2.99:
        return "Fail"
    elif 3.00 <= current_grade <= 3.49:
        return "Poor"
    elif 3.50 <= current_grade <= 4.49:
        return "Good"
    elif 4.50 <= current_grade <= 5.49:
        return "Very Good"
    elif 5.50 <= current_grade <= 6.00:
        return "Excellent"


grade = float(input())
print(corresponding_grade(grade))
