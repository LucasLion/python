

def give_bmi(h: list[int | float],
             w: list[int | float]) -> list[int | float]:

    try:
        if len(h) != len(w):
            raise ValueError("Length of h and w should be same")
        if len(h) == 0 or len(w) == 0:
            raise ValueError("Height and w list should not be empty")
        for i in range(len(h)):
            if not all(isinstance(val, (int, float)) for val in [h[i], w[i]]):
                raise ValueError("Height and w should be integer or float")
            if h[i] <= 0 or w[i] <= 0:
                raise ValueError("Height and w should be greater than 0")
    except ValueError as e:
        print(e)
        return []

    bmi_list = []
    for i in range(len(h)):
        bmi_list.append(w[i] / (h[i] ** 2))
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        if type(limit) not in [int, float]:
            raise ValueError("Limit should be integer or float")
        if limit <= 0:
            raise ValueError("Limit should be greater than 0")
    except ValueError as e:
        print(e)
        return []

    limit_list = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            limit_list.append(True)
        else:
            limit_list.append(False)
    return limit_list
