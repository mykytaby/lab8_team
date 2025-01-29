#Mykyta Bychenok
# Dictionary storing student performance
students = {
    "Group 101": [
        {
            "full_name": "Ivan Petrovich Ivanov",
            "course": 2,
            "subjects": {"Programming": [85, 90, 78], "Physics": [80, 75, 88]}
        },
        {
            "full_name": "Pavlo Andriyovych Shevchenko",
            "course": 2,
            "subjects": {"Programming": [75, 80, 72], "Physics": [85, 79, 90]}
        },
        {
            "full_name": "Olena Serhiivna Tkachenko",
            "course": 2,
            "subjects": {"Programming": [88, 92, 85], "Physics": [90, 88, 86]}
        },
        {
            "full_name": "Dmytro Mykolaiovych Bondarenko",
            "course": 2,
            "subjects": {"Programming": [70, 78, 65], "Physics": [75, 80, 82]}
        },
        {
            "full_name": "Kateryna Oleksandrivna Moroz",
            "course": 2,
            "subjects": {"Programming": [95, 97, 92], "Physics": [98, 95, 96]}
        },
        {
            "full_name": "Yurii Ivanovych Koval",
            "course": 2,
            "subjects": {"Programming": [82, 85, 80], "Physics": [84, 83, 86]}
        }
    ]
}

# Function to add a new student
def add_student(group, full_name, course, subjects):
    if group not in students:
        students[group] = []
    students[group].append({
        "full_name": full_name,
        "course": course,
        "subjects": subjects
    })

# Example of adding a new student
new_student = {
    "Programming": [85, 89, 84],
    "Physics": [74, 77, 73]
}
add_student("Group 101", "Olivia Taylor Jones", 2, new_student)

# Display students dictionary
print(students)
#Mykyta Bychenok
