
def fib():
    a = [1]
    yield a
    while True:
        temp = []
        a.insert(0,0)
        a.append(0)
        for i in range(0,len(a) -1):
            temp.append(a[i] + a[i+1])
        else:
            a= temp
        yield temp
f = fib()
for i in range(0,10):
   print(next(f))
