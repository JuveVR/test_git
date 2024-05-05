# Find the sum and product of the elements of the list greater than the number MIN and less than the number MAX (both boundaries inclusive).
#
# If there are no such elements, print None object for both the sum and the product.

# option 1
lst = [2, 4, 6, 2, 5, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6
filtered_list = []

multiply_result = 1
for i in lst:
    if MIN < i < MAX:
        multiply_result = multiply_result * i
        filtered_list.append(i)

if len(filtered_list) == 0:
    print("sum_: None object", "product: None object")
else:
    print(f"sum_: {sum(filtered_list)}, product: {multiply_result}" )


# option 2
filtered_list = [i for i in lst if MIN < i < MAX]

if not filtered_list:
    print("sum_:", None)
    print("product:", None)
else:
    sum_ = sum(filtered_list)
    multiply_result = 1
    for i in filtered_list:
        multiply_result *= i

    print("Sum:", sum_)
    print("Product:", multiply_result)

