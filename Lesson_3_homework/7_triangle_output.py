# Output a triangle of user-entered size.
#
# There are NO spaces at the end of lines.
#
# DO NOT use methods of string type.

#option 1
triangle_base = int(input("Hello! Enter size of triangle: "))
brick = "*"
empty_space = " "
t = 1
for t in range(0, triangle_base + 1):
    print(triangle_base * empty_space, brick * t)
    triangle_base -= 1
    t += 1

print("----------Divider---------")
#option 2
triangle_base_option_2 = int(input("Hello! Enter size of triangle: "))

for l in range(1, triangle_base_option_2 + 1):
      print(empty_space * (triangle_base_option_2 - l) + brick * l)