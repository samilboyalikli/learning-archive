
def others_list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(
        [
            [i,j,k]
            for i in range(x+1)
            for j in range(y+1)
            for k in range(z+1)
            if i+j+k != n
        ]
    )


def sb_list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i = [item for item in range(0,x+1)]
    j = [item for item in range(0,y+1)]
    k = [item for item in range(0,z+1)]

    all_combinations = [[a,b,c] for a in i for b in j for c in k]
    result = []

    for combination in all_combinations:
        if sum(combination) != n:
            result.append(combination)
    
    print(result)


def others_print_function():
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')


def sb_print_function():
    n = int(input())
    results = [i for i in range(1,n+1)]
    print(*results,sep='')


def others_loops():
    n = int(input())
    results = [i*i for i in range(n)]
    print(*results,sep='\n')


def sb_loops():
    n = int(input())
    for i in range(n):
        print(i*i)


def sb_python_division():
    a = int(input())
    b = int(input())
    print(f"{a//b}\n{a/b}")


def others_arithmetic_operations():
    a = int(input())
    b = int(input())
    results = [a+b,a-b,a*b]
    print(*results,sep='\n')


def sb_arithmetic_operations():
    a = int(input())
    b = int(input())
    print(f"{a+b}\n{a-b}\n{a*b}")


def others_python_if_else():
    n = int(input().strip())
    if n%2==1 or 6<=n<=20:
        print("Weird")
    elif 2<=n<=5 or n>=20:
        print("Not Weird")


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


if __name__ == '__main__':
    #sb_python_if_else() 
    #others_python_if_else()  
    #sb_arithmetic_operations()
    #others_arithmetic_operations()
    #sb_python_division()
    #sb_loops()
    #others_loops()
    #sb_print_function()
    #others_print_function()
    #sb_list_comprehensions()
    others_list_comprehensions()

