from gradebook import Gradebook

def menu():
    print("\n===== STUDENT GRADEBOOK CLI =====")
    print("1. Add Course")
    print("2. Update Course")
    print("3. Delete Course")
    print("4. View Gradebook")
    print("5. Calculate GPA")
    print("6. Calculate GPA by Semester")
    print("0. Exit")
    return input("Choose an option: ")

if __name__ == "__main__":
    gb = Gradebook()

    while True:
        choice = menu()

        if choice == "1":
            gb.add_course()

        elif choice == "2":
            gb.update_course()

        elif choice == "3":
            gb.delete_course()

        elif choice == "4":
            gb.view_gradebook()

        elif choice == "5":
            gb.calculate_gpa()

        elif choice == "6":
            semester = input("Enter semester: ")
            gb.calculate_gpa(semester=semester)

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
