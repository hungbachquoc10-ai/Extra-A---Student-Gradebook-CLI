+ Student Gradebook CLI:
A command-line Python application for managing student courses and calculating weighted GPA.
This program supports adding, updating, deleting, and viewing courses, as well as computing both overall GPA and semester-based GPA.

-  Main Features:
  + Add a Course:

Enter course code, name, credits, semester, and score.

Validates missing fields, invalid grades, and duplicate course codes.
  +  Update a Course:

Modify any field of an existing course by entering its course code.
 + Delete a Course:
Remove a course entry from the gradebook.
View Gradebook:
Displays all stored courses in a clean table format.
+  GPA Calculation:
Computes weighted GPA across:
All courses :
Specific semester 
 + Persistent Storage:
All course data is saved in gradebook.json.
Automatically loads data on program startup.
 - Requirements:
Python 3.12

- How to Run:

1.Clone or download the project files.
2. Open a terminal in the project directory.
3. Run:
