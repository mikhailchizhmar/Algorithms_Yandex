A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

answer = "NO"
min_edges = sorted([A, B, C])
if min_edges[0] <= D and min_edges[1] <= E or min_edges[0] <= E and min_edges[1] <= D:
    answer = "YES"

print(answer)
