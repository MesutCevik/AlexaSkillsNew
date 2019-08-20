from typing import Any
"""
None
'Definition: 
The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a datatype of its own (NoneType) and only None can be None.'
"""


def is_none_or_not_none_a(x: Any):
    # This function proves whether x is not None (it has any value or zero) or
    # it is None (it has no value not even a zero).
    if x is not None:
        print(f"x = {x}. x is not None.")
        # If x has not stored 'None' then do this.
    else:
        print(f"x = {x}. x is None, it has stored None. You see this text only when x has stored None.")
        # If x has stored 'None' then do this.


def is_none_or_not_none_b(x: Any):
    # This function proves whether x is True or False.
    if x:
        print(f"x = {x}. x is True, it has stored not 0, None or something empty.")
        # If x is True then do this. x is True when it has a value which is not 0 (zero) and not empty.
    else:
        print(f"x = {x}. x is False, it has stored 0, None or something empty.")
        # If x is False, that means x is not Ture, then do this. x is False when it has 0 (zero), None or an empty string.


if __name__ == '__main__':
    is_none_or_not_none_a(7)  # The VAR y is not None, it has the value 7.
    is_none_or_not_none_a(0)  # The VAR y None ( value 0 - that means it is not None.
    is_none_or_not_none_a(-5)  # The VAR y None ( value 0 - that means it is not None.
    is_none_or_not_none_a("")  # The VAR y has the value 0 - that means it is not None.
    is_none_or_not_none_a("g")  # The VAR y has the value 0 - that means it is not None.
    is_none_or_not_none_a(None)  # The VAR x has no value - that means it is None.

    print()
    is_none_or_not_none_b(7)  # The VAR y has the value 7 - that means it is not None.
    is_none_or_not_none_b(0)  # The VAR y has the value 0 - that means it is not None.
    is_none_or_not_none_b(-5)  # The VAR y has the value 0 - that means it is not None.
    is_none_or_not_none_b("")  # The VAR x has no value - that means it is None.
    is_none_or_not_none_b("g")  # The VAR x has no value - that means it is None.
    is_none_or_not_none_b(None)  # The VAR x has no value - that means it is None.
