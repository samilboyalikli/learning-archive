import dis


def function():
    a = "hello world"
    print(a)


dis.dis(function)
