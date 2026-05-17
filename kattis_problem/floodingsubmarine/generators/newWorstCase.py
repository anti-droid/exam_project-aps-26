n = 50000
e = 49999
h = 100
p = 100
print(n, e, h, p)

for i in range(n-h-1):
    print(i, i+1)

for i in range(n-h,n):
    print(n-h-1,i)

for i in range(n-h,n):
    print(i)