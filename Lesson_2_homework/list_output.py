# task
# Create list of 3 cats/dogs names
# Output elements using coma and space:

dogs_names = ["Tuzik", "Bobik", "Zhorik"]

# output option 1
print(*dogs_names, sep = ", ")

# output option 2
print(", ".join([str(name) for name in dogs_names]))

# output option 3
print(", ".join(dogs_names))

# output option 4
s = ""
for names in dogs_names[:-1]:
    s = s + str(names) + ', '
s = s + str(dogs_names[-1])
print(s)





