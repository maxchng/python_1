def check_list_type(list):
    """
    Check whether the item in the list are of int or float.
    Return true if it is, else return false.
    """
    for item in list:
        if not isinstance(item, (int, float)):
            return False
    return True


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
        ) -> list[int | float]:
    """
    To calculate BMI(Body Mass Index), weight / height**2.
    This function return the bmi based on the height and weight.
    """
    if len(height) != len(weight):
        print("Length are not the same.")
        return []
    elif not (check_list_type(height) and check_list_type(weight)):
        print("List has to only contain either an int or float.")
        return []
    return [weight[i] / (height[i] ** 2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of true or false based on the limit set by the user.
    if the bmi is higher than the limit return True, else return False.
    """
    if len(bmi) == 0:
        return []
    return [True if bmi[i] > limit else False for i in range(len(bmi))]
