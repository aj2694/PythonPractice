def fibo(num):
    a=1
    b=1
    for i in range(num):
        yield a
        a,b=b,a+b

num=int(input("Enter the length of Fibonacci series"))
for i in fibo(num):
    print(i)