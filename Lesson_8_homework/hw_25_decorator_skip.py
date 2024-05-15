# Write decorator skip_if that takes two arguments:
#
# - condition: boolean expression
#
# - reason: string, default value empty string
#
# If condition is calculated as True, function shouldn't be performed and if reason is not empty, reason should be printed
#
# If condition is False, then function should be performed as usual

def skip_if(condition, reason=""):
#def skip_if(condition: bool, reason: str = "")  # optional with anotations
    def decorator(fun):
        def wrapper(*args, **kwargs):
            if condition:
                if reason:
                    print(reason)
                return
            try:
                return fun(*args, **kwargs)  # It works also without Return here, is it ok to use it without return?
            except AssertionError:
                print("Assertion Error")
        return wrapper
    return decorator


@skip_if(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5


test_two_plus_two()


@skip_if(condition=True, reason='')
def test_two_plus_two():
    assert 2 + 2 == 5


test_two_plus_two()


@skip_if(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_minus_two():
    assert 2 - 2 == 5


test_two_minus_two()  # assertion error
