from typing import Any
"""
None
'Definition: 
The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a datatype of its own (NoneType) and only None can be None.'
"""


def is_none_or_not_none(x: Any):
    print()
    if x is not None:
        print(f"The value of x is: {x}. It has a value, it is not 'None'.")
    else:
        print(f"The value of x is: {x}. It has no value, it is 'None'.")


if __name__ == '__main__':
    # The VAR y has the value 7 - that means it is not None.
    is_none_or_not_none(7)

    # The VAR y has the value 0 - that means it is not None.
    is_none_or_not_none(0)

    # The VAR x has no value - that means it is None.
    is_none_or_not_none(None)

    # The VAR x has no string value - that means it is None.
    is_none_or_not_none('')

    # The VAR x has no string value - that means it is None.
    is_none_or_not_none([])

    # The VAR x has no string value - that means it is None.
    is_none_or_not_none({})

    # The VAR x has no string value - that means it is None.
    is_none_or_not_none(())
