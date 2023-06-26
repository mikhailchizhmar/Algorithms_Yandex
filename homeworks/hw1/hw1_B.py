a = int(input())
b = int(input())
c = int(input())
flag = "NO"

if a * b * c <= 0:
    flag = "NO"
elif a + b <= c or a + c <= b or b + c <= a:
    flag = "NO"
else:
    flag = "YES"
print(flag)
