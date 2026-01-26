# import random
# names = [
#     "Liam", "Olivia", "Noah", "Emma", "Aiden", "Sophia", "Jackson", "Isabella",
#     "Lucas", "Mia", "Ethan", "Charlotte", "Mason", "Amelia", "Logan", "Harper",
#     "James", "Evelyn", "Benjamin", "Abigail"
# ]
# student_marks = {student:random.randint(0,100) for student in names }
#
# passed_students = {student: score for student, score in student_marks.items() if score >= 60}
# print(passed_students)

weekly_temps_bd = {
    "Monday": 25.0,    # ~77°F → ~25.0°C
    "Tuesday": 25.0,   # ~77°F → ~25.0°C
    "Wednesday": 25.0, # ~77°F → ~25.0°C
    "Thursday": 25.0,  # ~77°F → ~25.0°C
    "Friday": 26.1,    # ~79°F → ~26.1°C
    "Saturday": 27.2,  # ~81°F → ~27.2°C
    "Sunday": 27.8     # ~82°F → ~27.8°C
}
temp_f = {day:((temp*9/5)+32) for (day,temp) in weekly_temps_bd.items()}
print(temp_f)