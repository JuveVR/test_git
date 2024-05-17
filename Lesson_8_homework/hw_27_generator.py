# Write generator function that takes two arguments:
#
# lst - list
#
# iter_num - integer with default value None
#
# Generator should return items from the list one by one. When generator comes to the last item, it should start from the beginning and repeat it iter_num times.
#
# If iter_num is None, generator should return items infinitely

def my_generator(lst, iter_num=None):
    if iter_num is None:
        while True:
            for item in lst:
                yield item
    else:
        for _ in range(iter_num):
            for item in lst:
                yield item


lst = ['a', 'b']
for i in my_generator(lst):
    print(i)
