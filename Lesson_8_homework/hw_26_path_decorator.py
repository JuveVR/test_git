# Write decorator call_counter that takes path to file as argument.
#
# Decorated function should log total number of calls to passed file.
#
# Several functions could log to the same file.

def call_counter(path):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            fun_name = fun.__name__
            with open(path, "a") as func_logging:
                func_logging.write(f"Function {fun_name} was called {wrapper.calls} times\n")
            return fun(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator


@call_counter('/Users/vadymr/python_project/python_lerning/Lesson_8_homework/logging_functions.txt')
def add(a, b):
    return a + b


@call_counter('/Users/vadymr/python_project/python_lerning/Lesson_8_homework/logging_functions.txt')
def add_more(a, b):
    return a + b


print(add(4, 6))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
print(add_more(3, 5))
print(add_more(3, 5))
print(add_more(3, 5))
print(add(3, 5))
print(add_more(3, 5))