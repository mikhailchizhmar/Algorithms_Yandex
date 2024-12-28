a = int(input())
b = int(input())
c = int(input())
flag = "YES"

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    flag = "NO"
print(flag)
