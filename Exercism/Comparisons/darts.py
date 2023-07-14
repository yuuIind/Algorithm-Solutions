def score(x, y):
    r = (x**2 + y**2)**0.5
    inner_circle = 1
    middle_circle = 5
    outer_circle = 10
    if r <= inner_circle:
        return 10
    elif inner_circle < r <= middle_circle:
        return 5
    elif middle_circle < r <= outer_circle:
        return 1
    else:
        return 0
