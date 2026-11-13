students = {
    "101": {
        "name": "Arun",
        "dept": "CSE",
        "marks": {
            "Python": 90,
            "Java": 85,
            "Maths": 95,
        },
    },
    "102": {
        "name": "Priya",
        "dept": "ECE",
        "marks": {
            "Python": 80,
            "Java": 90,
            "Maths": 85,
        },
    },
    "103": {
        "name": "Kumar",
        "dept": "IT",
        "marks": {
            "Python": 75,
            "Java": 80,
            "Maths": 70,
        },
    },
}


def register_student(roll, name, dept):
    if roll not in students:
        students[roll] = {
            "name": name,
            "dept": dept,
            "marks": {},
        }
        print("Student Registered Successfully!")
    else:
        print("Student Already Exists!")


def add_marks(roll, subject, mark):
    if roll in students:
        students[roll]["marks"][subject] = mark
        print("Marks Added Successfully!")
    else:
        print("Student Not Found!")


def update_marks(roll, subject, mark):
    if roll in students:
        if subject in students[roll]["marks"]:
            students[roll]["marks"][subject] = mark
            print("Marks Updated Successfully!")
        else:
            print("Subject Not Found!")
    else:
        print("Student Not Found!")


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def calculate_result(roll):
    if roll in students:
        marks = students[roll]["marks"]

        if len(marks) == 0:
            print("Marks Not Available!")
            return

        total = sum(marks.values())
        avg = total / len(marks)
        grade = calculate_grade(avg)

        print("\nStudent Name:", students[roll]["name"])
        print("Roll Number:", roll)
        print("Department:", students[roll]["dept"])
        print("Subject Marks:", marks)
        print("Total Marks:", total)
        print("Average Marks:", round(avg, 2))
        print("Grade:", grade)
    else:
        print("Student Not Found!")


def search_student(roll):
    if roll in students:
        print("\nStudent Found!")
        calculate_result(roll)
    else:
        print("Student Not Found!")


def display_students():
    for roll, details in students.items():
        print("\nRoll Number:", roll)
        print("Name:", details["name"])
        print("Department:", details["dept"])
        print("Marks:", details["marks"])


def class_topper():
    topper = None
    highest_avg = -1

    for roll, details in students.items():
        marks = details["marks"]

        if marks:
            avg = sum(marks.values()) / len(marks)

            if avg > highest_avg:
                highest_avg = avg
                topper = roll

    if topper is not None:
        print("\n----- CLASS TOPPER -----")
        print("Name:", students[topper]["name"])
        print("Roll Number:", topper)
        print("Department:", students[topper]["dept"])
        print("Average:", round(highest_avg, 2))
        print("Grade:", calculate_grade(highest_avg))
    else:
        print("No Marks Available!")


def main():
    print("===== STUDENT MANAGEMENT SYSTEM =====")

    register_student("104", "Divya", "CSE")

    add_marks("104", "Python", 95)
    add_marks("104", "Java", 90)
    add_marks("104", "Maths", 85)

    update_marks("102", "Python", 95)

    print("\n===== STUDENT RESULT =====")
    calculate_result("101")

    print("\n===== SEARCH STUDENT =====")
    search_student("102")

    print("\n===== ALL STUDENTS =====")
    display_students()

    print("\n===== CLASS TOPPER =====")
    class_topper()


if __name__ == "__main__":
    main()
