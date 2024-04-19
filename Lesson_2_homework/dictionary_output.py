# Create list of 3 countries names.
# Create dictionary of 3 key-value pairs.
# Key should be country name from the list and value should be string with its capital.
# Output each pair on separate lines. Separate key from value with colon and space:


next_destinations = ["Mexico", "Kosta rica", "Cuba"]

destinations_capitals = {
    next_destinations[0]: "Mexico city",
    next_destinations[1]: "San Jose",
    next_destinations[2]: "Havana"
}
# option_1
for key, value in destinations_capitals.items():
    print(key, value, sep= ": ")

# option_2
new_lines = [f'{key}:  {value}' for key, value in destinations_capitals.items()]
print('\n'.join(new_lines))

# option_3
a_1 = next_destinations[0]
a_2 = destinations_capitals.get(next_destinations[0])
a = next_destinations[0] + ": " + destinations_capitals.get(next_destinations[0])
b = next_destinations[1] + ": " + destinations_capitals.get(next_destinations[1])
c = next_destinations[2] + ": " + destinations_capitals.get(next_destinations[2])
d = [a, b, c]
print('\n'.join(d))