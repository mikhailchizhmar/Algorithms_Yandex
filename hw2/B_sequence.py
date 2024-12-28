STOP_NUM = -2000000000

prev = int(input())
if prev == STOP_NUM:
    print("CONSTANT")
else:
    is_constant = True
    is_ascending = True
    is_weakly_ascending = True
    is_descending = True
    is_weakly_descending = True

    while True:
        current = int(input())
        if current == STOP_NUM:
            break

        if current > prev:
            is_constant = False
            is_descending = False
            is_weakly_descending = False
        elif current < prev:
            is_constant = False
            is_ascending = False
            is_weakly_ascending = False
        else:
            is_ascending = False
            is_descending = False

        prev = current

    if is_constant:
        print("CONSTANT")
    elif is_ascending:
        print("ASCENDING")
    elif is_weakly_ascending:
        print("WEAKLY ASCENDING")
    elif is_descending:
        print("DESCENDING")
    elif is_weakly_descending:
        print("WEAKLY DESCENDING")
    else:
        print("RANDOM")
