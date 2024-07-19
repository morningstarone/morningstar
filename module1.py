import calculator as c
a=list(map(int,input().split()))
inp=int(input('enter operation: 1. add 2. multiply 3. subtract 4. divide'))
if inp==1:
    print(c.add(a[0],a[1]))
elif inp==2:
    print(c.multiply(a[0],a[1]))
elif inp==3:
    print(c.subtract(a[0],a[1]))
elif inp==4:
    print(c.divide(a[0],a[1]))
