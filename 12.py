a = int(input())
b = int(input())
c = int(input())
d = (a * b) - c
if(c > a + b):
    print("NO")
elif(d % a == 0) or (d % b == 0):
    print("YES")
else:
    print("NO")