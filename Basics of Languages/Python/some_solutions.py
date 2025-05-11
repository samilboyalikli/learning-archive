
def sb_python_if_else():
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    else:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")   


def others_python_if_else():
    n = int(input().strip())
    if n%2==1 or 6<=n<=20:
        print("Weird")
    elif 2<=n<=5 or n>=20:
        print("Not Weird")


def sb_arithmetic_operations():
    a = int(input())
    b = int(input())
    print(f"{a+b}\n{a-b}\n{a*b}")


def others_arithmetic_operations():
    a = int(input())
    b = int(input())
    results = [a+b,a-b,a*b]
    print(*results,sep='\n')


if __name__ == '__main__':
    #sb_python_if_else() 
    #others_python_if_else()  
    #sb_arithmetic_operations()
    others_arithmetic_operations()

