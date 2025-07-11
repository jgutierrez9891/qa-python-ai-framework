# LIST OF DICTIONARIES - CREATED DYNAMICALLY

people = []
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    people.append({"name": name, "age": age})

print(people)

# LIST OF DICTIONARIES - NESTED STRUCTURE

students = [
    {"name": "John", "grades": [90, 85, 88]},
    {"name": "Jane", "grades": [92, 81, 79]}
]

# LAMBDA FUNCTION - BASIC LAMBDA

for student in students:
    print(f"{student['name']} has grades: {student['grades']}")

add = lambda x, y: x + y
print(add(2, 3)) 