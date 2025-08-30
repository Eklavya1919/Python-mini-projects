n = 5
for i in range(1,n+1):
    print("*"*i)

print()
print()
print()

for i in range(n,0,-1):
    print("*"*i)

print()
print()
print()

for i in range(1,n+1):
    print((" "*(n-i))+"*"*i)

print()
print()
print()

for i in range(n,0,-1):
    print((" "*(n-i))+"*"*i)

print()
print()
print()

for i in range(1,n+1):
    print((" "*(n-i))+"*"*(2*i-1))

print()
print()
print()

for i in range(n,0,-1):
    print((" "*(n-i))+"*"*(2*i-1))

print()
print()
print()

for i in range(1,n+1):
    print((" "*(n-i))+"*"*(2*i-1))
for i in range(n-1,0,-1):
    print((" "*(n-i))+"*"*(2*i-1))

print()
print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print()
print()

n = 11
mid = n // 2

for i in range(n):
    for j in range(n):
        if (
            i == mid or j == mid or
            (i == 0 and j >= mid) or
            (i == n - 1 and j <= mid) or
            (j == 0 and i <= mid) or
            (j == n - 1 and i >= mid)
           ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()