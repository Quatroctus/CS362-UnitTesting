
def volume_cube(length):
    if length < 0:
        raise ValueError()
    if isinstance(length, float) or isinstance(length, int):
        return abs(length ** 3)
    raise TypeError()
