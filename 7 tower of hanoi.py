def toh(n,a,b,c):
    if n>0:
        toh(n-1,a,c,b)
        if a:
            c.append(a.pop())
        toh(n-1,b,a,c)
