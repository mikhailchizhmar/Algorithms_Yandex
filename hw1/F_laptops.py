a1, b1, a2, b2 = map(int, input().split())

if a1 < b1:
    a1, b1 = b1, a1
if a2 < b2:
    a2, b2 = b2, a2

S1 = (a1 + b2) * max(b1, a2)
S2 = (b1 + b2) * max(a1, a2)
S3 = (a2 + b1) * max(a1, b2)
S4 = (a2 + a1) * max(b1, b2)
S_min = min(S1, S2, S3, S4)

# S_min == S4
a_final = max(b1, b2)
b_final = S4 // a_final

if S_min == S1:
    a_final = max(b1, a2)
    b_final = S1 // a_final
elif S_min == S2:
    a_final = max(a1, a2)
    b_final = S2 // a_final
elif S_min == S3:
    a_final = max(a1, b2)
    b_final = S3 // a_final

print(a_final, b_final)
