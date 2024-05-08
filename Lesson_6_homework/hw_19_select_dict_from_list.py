# There is a list consisting of dictionaries. Each dictionary describes a user and has two keys: 'name' (str) and 'age' (int).
#
# Create and output a list of users' names whose age is 18 years (including) or older.

#option 1
users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19},
    {'name': 'Vad Rov',
     'age': 12},
    {'name': 'Grisha Toj',
     'age': 22}
]

old_school = []
old_school_names =[]
for student in users:
    if student["age"] >= 18:
        old_school.append(student)

for i in old_school:
    old_school_names.append(i["name"])

print("Result:", old_school_names)


# option 2
old_school_names =[]

for student in users:
    if student['age'] >= 18:
        old_school_names.append(student['name'])

print(f"Result: {old_school_names}")