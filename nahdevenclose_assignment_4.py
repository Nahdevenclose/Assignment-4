"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Nahdia Benson
GitHub Username: Nahdevenclose
Date: 13 Februrary 2026
Description: This program simulates a college life adventure game where the player makes choices that affect their GPA, study hours, social points, and stress level. The player starts with a certain GPA, study hours, social points, and stress level, and then chooses a course load that impacts these attributes. The game provides feedback on how the player's choices affect their college life experience.
AI Usage: [Describe any AI assistance OR write "None"]
"""

# ========================================
# Decision 1: Course Load Selection
# ========================================

#Predetermined values for the student
student_name = "Nahdia Benson"  # Replace with your actual name
current_gpa = 2.99 # Float between 1.0-4.0
study_hours = 25 # Integer (e.g., 25)
social_points = 50 # Integer (e.g., 50)
stress_level = 90 # Integer 0-100

#Welcome message and showing the initial stats of the student
print("Welcome", student_name)
print("Your current GPA is", current_gpa, "with", study_hours, "hours of study per week.")
print("You have", social_points, "social points and a stress level of", stress_level)
print("Welcome to the Student Life Simulator! Let's see how your choices affect your life as a student <3")

print("Choose a course load:")
print("\t 1. Light (4 courses)")
print("\t 2. Standard (6 courses)")
print("\t 3. Heavy (8 courses)")

course_load_choice = int(input("Enter the number corresponding to your choice: "))

if course_load_choice <= 4:
    print("You chose a Light course load. This will allow you to focus more on each class and maintain a better work-life balance.")
    current_gpa += 0.2
    study_hours += 5
    social_points += 10
    stress_level -= 10
    print(f"Your GPA has increased to {current_gpa:.2f}")
    print("Your study hours have increased to", study_hours)
    print("Your social points have increased to", social_points)
    print("Your stress level has decreased to", stress_level)
elif 4 < course_load_choice <= 6:
    print("You chose a Standard course load. This is a balanced choice that allows you to manage your time effectively while still challenging yourself.")
    current_gpa += 0.1
    study_hours += 10
    social_points += 5
    stress_level -= 5
    print(f"Your GPA has increased to {current_gpa:.2f}")
    print("Your study hours have increased to", study_hours)
    print("Your social points have increased to", social_points)
    print("Your stress level has decreased to", stress_level)
elif 6 < course_load_choice <= 8:
    print("You chose a Heavy course load. This will be very challenging and may lead to increased stress, but it can also boost your GPA if you manage it well.")
    current_gpa += 0.05
    study_hours += 15
    social_points -= 10
    stress_level += 20
    print(f"Your GPA has increased to {current_gpa:.2f}")
    print("Your study hours have increased to", study_hours)
    print("Your social points have decreased to", social_points)
    print("Your stress level has increased to", stress_level)
else:
    print("Invalid choice. Please choose a valid course load.")
