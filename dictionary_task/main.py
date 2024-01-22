from students import studentsList


def main():
    for student in studentsList:
        sum_of_subjects = 0
        for marks in student['subjects'].values():
            sum_of_subjects += marks

        student['total_marks'] = sum_of_subjects
        print(
            f"Name: {student['name']}, Subjects: {student['subjects']}, Total Marks: {sum_of_subjects}")


if __name__ == "__main__":
    main()
