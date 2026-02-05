def fib():
    a,b = 0,1

    while True:
        yield a
        a, b = b, a+b


if __name__== "__main__":
    for f in fib():
        if f> 50:
            break
        print(f)