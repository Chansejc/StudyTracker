def list_to_entry(lst):
    to_add = ''
    x = 0
    for i in lst:
        if type(i) == int:
            to_add += str(i)
            continue
        to_add += f"'{i}'"
        if len(lst) - 1 != x:
            to_add += ","
        x += 1
    return to_add
