
def full_name(first, last):
    if isinstance(first, str) and isinstance(last, str):
        return ' '.join([first, last])
    return None
