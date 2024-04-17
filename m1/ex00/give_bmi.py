

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    try:
        if len(height) != len(weight):
            raise ValueError("Length of height and weight should be same")
        if len(height) == 0 or len(weight) == 0:
            raise ValueError("Height and weight list should not be empty")
        for i in range(len(height)):
            if type(height[i]) not in [int, float] or type(weight[i]) not in [int, float]:
                raise ValueError("Height and weight should be integer or float")
            if height[i] <= 0 or weight[i] <= 0:
                raise ValueError("Height and weight should be greater than 0")
    except ValueError as e:
        print(e)
        return []

    bmi_list = []
    for i in range(len(height)):
        bmi_list.append(weight[i] / (height[i] ** 2))
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
