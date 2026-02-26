# Task 1  Process the Scores
def process_scores(details):
    result = {}

    for name, marks in details.items():
        average_score = round(sum(marks) / len(marks), 2)
        result[name] = average_score
    return result


students_scores = {
    "Priya": [85, 90, 78],
    "Bala": [70, 88, 92],
    "Nandhu": [95, 80, 85],
    "Karthi": [60, 75, 70],
    "Surya": [88, 91, 84],
}
result = process_scores(students_scores)
print(result)


# Task 2 Classify the Grades
def classify_grades(average):
    report = {}

    for name, score in average.items():
        if score >= 90:
            grade = "Grade A"
        elif score < 89 and score >= 75:
            grade = "Grade B"
        elif score < 74 and score >= 60:
            grade = "Grade C"
        elif score < 60:
            grade = "Grade F"

        report[name] = (score, grade)

    return report


grades = classify_grades(result)
print(grades)


# Task 3 Generate the Report
def generate_report(classified, passing_avg=70):
    print()
    total_students = len(classified)
    passed = 0
    failed = 0
    print("===== Student Grade Report =====")

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1

        else:
            failed += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade[-1]} | Status: {status}")

    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")


grade_report = generate_report(grades)
