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