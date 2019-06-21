import math


def foo(func):
    print("The function " + func.__name__ + " was passed to foo.")
    result = 0
    for x in [1, 2, 2.5]:
        result += func(x)
        print(result)
    return result


print(foo(math.sin))
print(foo(math.cos))
