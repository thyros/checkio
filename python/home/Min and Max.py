"""
In this mission you should write you own py3 implementation (but you can use py2 for this)
of the built-in functions min and max.
Some builtin functions are closed here: import, eval, exec, globals.
Don't forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable.
The largest (smallest) item in the iterable is returned.
If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument that is used to extract
a comparison key from each list element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.

Example:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

How it is used: This task will help you understand how some of the built-in functions work on a more precise level.

Precondition: All test cases are correct and functions don't have to raise exceptions.
"""
import types

def nomalise_args(*args):
    # turn args to a single level list
    new_args = [None]
    while len(new_args) == 1:
        new_args = list(args[0])
        if isinstance(new_args, types.GeneratorType):
            new_args = list(new_args)
        if new_args == args[0] or type(new_args[0]) in [int, float]:
            break
        args = new_args
    return new_args

def transform_arguments(args, key):
    return [key(arg) for arg in args]

def find_value(args, biggest):
    value = args[0]
    index = 0

    for i, arg in enumerate(args):
        if (biggest and arg > value) or (not biggest and arg < value):
            index = i
            value = arg

    return index

def find(args, key, biggest):
    nomalised_args = nomalise_args(args)
    if key:
        transformed_args = transform_arguments(nomalised_args, key)
    else:
        transformed_args = nomalised_args

    index = find_value(transformed_args, biggest)
    return nomalised_args[index]

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return find(args, key, False)

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return find(args, key, True)


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("all done")