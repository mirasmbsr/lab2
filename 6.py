
a = int(input())

b = int(input())

c = int(input())

if (a==b and a==c):

    print("3")

elif((a!=b and a==c) or (a==b and a!=c) or (c==b and c!=a)):

    print("2")

else:

    print("0")