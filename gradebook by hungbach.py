import json
import os

class Gradebook:
    def __init__(self, filename="gradebook.json"):
        self.filename = filename
        self.courses = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.courses = json.load(f)
            except:
                print("Error loading JSON file. Starting with empty gradebook.")
                self.courses = []
        else:
            self.courses = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.courses, f, indent=4)

    def validate_course(self, code, name, credits, semester, score):
        if not code or not name or not semester:
            print("Error: Missing required fields.")
            return False

        if any(c["course_code"] == code for c in self.courses):
            print("Error: Duplicate course code.")
            return False

        if not credits.isdigit() or int(credits) < 1:
            print("Credits must be a positive number.")
            return False

        if not score.isdigit() or not (0 <= int(score) <= 100):
            print("Score must be between 0 and 100.")
            return False

        return True

    def add_course(self):
        print("\n--- Add Course ---")
        code = input("Course Code: ")
        name = input("Course Name: ")
        credits = input("Credits: ")
        semester = input("Semester: ")
        score = input("Score (0–100): ")

        if not self.validate_course(code, name, credits, semester, score):
            return

        course = {
            "course_code": code,
            "course_name": name,
            "credits": int(credits),
            "semester": semester,
            "score": int(score)
        }

        self.courses.append(course)
        self.save_data()
        print("Course added successfully!")

    def update_course(self):
        print("\n--- Update Course ---")
        code = input("Enter course code to update: ")

        for course in self.courses:
            if course["course_code"] == code:
                print("Leave fields empty to keep current value.")

                name = input(f"Course Name ({course['course_name']}): ") or course["course_name"]
                credits = input(f"Credits ({course['credits']}): ") or course["credits"]
                semester = input(f"Semester ({course['semester']}): ") or course["semester"]
                score = input(f"Score ({course['score']}): ") or course["score"]

                if isinstance(credits, str) and not credits.isdigit():
                    print("Invalid credits.")
                    return
                if isinstance(score, str) and not score.isdigit():
                    print("Invalid score.")
                    return

                course["course_name"] = name
                course["credits"] = int(credits)
                course["semester"] = semester
                course["score"] = int(score)

                self.save_data()
                print("Course updated successfully!")
                return

        print("Course not found.")

    def delete_course(self):
        print("\n--- Delete Course ---")
        code = input("Enter course code to delete: ")

        for course in self.courses:
            if course["course_code"] == code:
                self.courses.remove(course)
                self.save_data()
                print("Course deleted successfully!")
                return

        print("Course not found.")

    def view_gradebook(self):
        print("\n--- Gradebook ---")

        if not self.courses:
            print("Gradebook is empty.")
            return

        print("+--------+----------------------------+---------+------------+-------+")
        print("| Code   | Course Name                | Credits | Semester   | Score |")
        print("+--------+----------------------------+---------+------------+-------+")

        for c in self.courses:
            print(f"| {c['course_code']:<6} | {c['course_name']:<26} | {c['credits']:^7} | {c['semester']:<10} | {c['score']:^5} |")

        print("+--------+----------------------------+---------+------------+-------+")

    def calculate_gpa(self, semester=None):
        print("\n--- GPA Calculation ---")

        courses = self.courses
        if semester:
            courses = [c for c in self.courses if c["semester"] == semester]

            if not courses:
                print("No courses found for that semester.")
                return

        total_credits = sum(c["credits"] for c in courses)
        weighted = sum(c["credits"] * c["score"] for c in courses)

        if total_credits == 0:
            print("No credits found.")
            return

        gpa = weighted / total_credits
        if semester:
            print(f"GPA for {semester}: {gpa:.2f}")
        else:
            print(f"Overall GPA: {gpa:.2f}")
