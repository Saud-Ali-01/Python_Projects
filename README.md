# Python_Project
Student Performance Anlytics System
Overview
The Student Performance Analytics System is an automated Python-based solution engineered to process, evaluate, and derive meaningful insights from student academic records. It leverages the power of Pandas for data manipulation and NumPy for numerical operations to streamline grading and performance analytics.
Key Features & Functionality
 Performance Metrics: Computes the ⁠Total_Marks⁠ and average scores for each student across core subjects (Math, Science, English, and History).
 Grading System: Dynamically assigns academic grades (A, B, C, D) using a structured grading logic based on individual averages.
 Pass/Fail Evaluation: Implements a strict conditional rule where a student must score 40 or above in all subjects to be marked as 'PASS'; otherwise, they are designated as 'FAIL'.
 Statistical Analysis: Generates subject-wise performance aggregates, identifying the mean, maximum, and minimum scores for each subject.
 Top Performer Identification: Sorts and extracts the top 3 students based on their accumulated total marks, offering visibility into high achievers.
 Version Control: Fully integrated with Git and GitHub, ensuring robust repository management and collaboration.
Technology Stack
 Programming Language: Python 3.x
 Core Libraries: Pandas, NumPy
 Development Environment: VS Code
 Data Format: CSV
File Architecture & Logic
 ⁠student.csv⁠: Serves as the primary database housing raw student data including ⁠StudentId⁠, ⁠Name⁠, ⁠Attendance_Percentage⁠, and subject-specific marks.
 ⁠functions.py⁠: Contains the underlying logic and class definitions. The ⁠marks⁠ class computes totals and averages across columns, while the ⁠Grade⁠ and ⁠Status⁠ functions enforce evaluation rules.
 ⁠main.py⁠: The main controller script that executes the loading process, invokes the analysis pipeline, and outputs the processed student data along with performance summaries
