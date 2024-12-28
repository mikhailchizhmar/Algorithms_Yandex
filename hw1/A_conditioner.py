troom, tcond = map(int, input().split())
mode = input()
t = troom

if mode == "freeze":
    if troom <= tcond:
        t = troom
    else:
        t = tcond
    # easier: t = min(troom, tcond)
elif mode == "heat":
    if troom >= tcond:
        t = troom
    else:
        t = tcond
#     easier: t = max(troom, tcond)
elif mode == "auto":
    t = tcond
elif mode == "fan":
    t = troom

print(t)
