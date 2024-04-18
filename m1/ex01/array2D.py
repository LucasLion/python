def get_shape(array: list) -> tuple:
    return (len(array), len(array[0]))


def slice_me(family: list, start: int, end: int) -> list:
    try:
        for member in family:
            if not isinstance(member, list):
                raise ValueError("Each member of the family should be a list")
            if not all(isinstance(value, (int, float)) for value in member):
                raise ValueError("Each member of the family \
                should have numerical values")
            if len(member) != 2:
                raise ValueError("Each member \
                of the family should have 2 values")
    except ValueError as e:
        print(e)
        return []
    shape = get_shape(family)
    print(f"My shape is : {shape}")
    new_family = family[start:end]
    new_shape = get_shape(new_family)
    print(f"My new shape is : {new_shape}")
    return new_family
