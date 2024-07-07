import dis


def function():
    a = 40
    b = 60
    c = a + b
    print(c)


dis.dis(function)
