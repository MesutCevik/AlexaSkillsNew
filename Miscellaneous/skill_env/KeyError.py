
def key_error_handling_raw():
    # Create dictionary with three entries.
    values = {"a": 1, "b": 2, "c": 3}

    # Using the value directly can cause an error.
    try:
        print(values["d"])
    except KeyError:
        print("KeyError encountered!")

    # We use get()-method to safely get a value.
    print(values.get("d"))


def key_error_handling():
    # Create dictionary with three entries.
    values = {"a": 1, "b": 2, "c": 3}  # 'key: value'

    # Using the value directly can cause an error.
    try:
        print(f"The value of the key 'values['c']' is: {values['d']}")
    except KeyError:
        print("KeyError encountered, while trying to access a key, which supposedly doesn´t exists.")

    # Free line as space:
    print()

    # We use the get()-method to safely get a value.
    print(f"I am trying to get the value of the key values['d'], which supposedly doesn´t exists. "
          f"The feedback for this request is: {values.get('d')}")


if __name__ == '__main__':
    key_error_handling()
    print()
    key_error_handling_raw()
