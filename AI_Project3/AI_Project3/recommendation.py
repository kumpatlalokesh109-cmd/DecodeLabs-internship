items = {
    "Python Programming": [
        "Python Crash Course"
    ],
    "AI": [
        "Machine Learning Basics",
        "AI for Everyone"
    ],
    "Mobile Development": [
        "Flutter Development",
        "Firebase Guide"
    ],
    "Data Science": [
        "Data Science Handbook"
    ],
    "Data Analysis": [
        "Excel for Beginners"
    ]
}

print("Available Interests:")
for key in items:
    print("-", key)

interest = input("\nEnter your interest: ")

if interest in items:
    print("\nRecommended Items:")
    for item in items[interest]:
        print(item)
else:
    print("No recommendation found.")