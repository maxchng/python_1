def check_list_size(family):
    """
    Check if the size of the list are similar.
    If it's not return False, else return True.
    """
    first_item = family[0]
    for item in family:
        if len(first_item) != len(item):
            return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice the list into the specify shape and return it.
    """
    if type(family) is not list:
        print("'family' should be of type list.")
        return []
    if not check_list_size(family):
        print("List sizes are not the same.")
        return []
    shape = (len(family), len(family[0]))
    new_shape = (len(family[start:end]), len(family[start:end][0]))
    print(f"My shape is : {shape}")
    print(f"My new shape is : {new_shape}")
    return family[start:end]
