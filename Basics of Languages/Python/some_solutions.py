
def sb_text_alignment():
    thickness = int(input())
    
    for i in range(thickness):
        print(('H'*i).rjust(thickness-1)+'H'+('H'*i).ljust(thickness-1))

    for i in range(thickness+1): 
        print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6))

    for i in range((thickness+1)//2):
        print(('H'*thickness*5).center(thickness*6))    

    for i in range(thickness+1):
        print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6))    

    for i in range(thickness):
        print(
            (
                ('H'*(thickness-i-1)).rjust(thickness)
                +'H'+
                ('H'*(thickness-i-1)).ljust(thickness)
            ).rjust(thickness*6)
        )


def others_string_validators():
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


def sb_string_validators():
    s = input()
    qualifications = [
        [True for i in list(s) if i.isalnum()],
        [True for i in list(s) if i.isalpha()],
        [True for i in list(s) if i.isdigit()],
        [True for i in list(s) if i.islower()],
        [True for i in list(s) if i.isupper()]
    ]
    
    for qualification in qualifications:
        if True in qualification:
            print("True")
        else:
            print("False")


def sb_find_a_string(string,sub_string):
    return sum(1 for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string)


def find_a_string_main():
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string) #sb_find_a_string()
    print(count)


def others_mutations(string,position,character):
    return string[:position]+character+string[position+1:]


def sb_mutations(string,position,character):
    list_version_of_word = list(string)
    list_version_of_word[position] = f'{character}'
    return ''.join(list_version_of_word)


def mutations_main():
    s = input()
    i,c = input().split()
    s_new = mutate_string(s,int(i),c) #sb_mutations() or others_mutations()
    print(s_new)


def others_whats_your_name(first_name_of_user,second_name_of_user):
    return print(f"Hello, {} {}! You just delved into Python.".format(first_name_of_user,second_name_of_user))


def sb_whats_your_name(first_name,second_name):
    return print(f"Hello, {first_name} {second_name}! You just delved into Python.")


def whats_your_name_main():
    first_name = input()
    last_name = input()
    print_full_name(first_name,last_name) #sb_whats_your_name() or others_whats_your_name()


def sb_string_and_join(line):
    return '-'.join(line.split(' '))


def string_and_join_main():
    line = input()
    result = split_and_join(line) #sb_string_and_join()
    print(result)


def others_sWAPcASE():
    return s.swapcase()


def sb_sWAPcASE():
    s = s.swapcase()
    return s


def sWAPcASE_main():
    s = input()
    result = swap_case(s) #sb_sWAPcASE() or others_sWAPcASE()
    print(result)


def sb_tuples():
    n = int(input())
    integer_list = map(int,input().split())
    print(hash(tuple(integer_list)))


def others_lists():
    N = int(input())
    numbers = []

    commands = {
        "insert": lambda x: numbers.insert(x[0],x[1]),
        "print": lambda x: print(numbers),
        "remove": lambda x: numbers.remove(x[0]),
        "append": lambda x: numbers.append(x[0]),
        "sort": lambda x: numbers.sort(),
        "pop": lambda x: numbers.pop(),
        "reverse": lambda x: numbers.reverse(),
    }
    
    for _ in range(N):
        command = input().strip().split()
        cmd,args = command[0], list(map(int,command[1:]))
        
        if cmd in commands:
            commands[cmd](args)


def sb_lists():
    N = int(input())
    result = []
    
    for _ in range(N):
        command = input()
        if "insert" in command:
            numbers = command[6:].split()
            index,new_number = map(int,numbers)
            result.insert(index,new_number)
        elif "print" in command:
            print(result)
        elif "remove" in command:
            result.remove(int(command[7]))
        elif "append" in command:
            result.append(int(command[7]))
        elif "sort" in command:
            result.sort()
        elif "pop" in command:
            result.pop()
        elif "reverse" in command:
            result.reverse()


def others_finding_the_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float,line))
        student_marks[name] = scores
    query_name = input()
    
    result = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{o:.2f}")


def sb_finding_the_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float,line))
        student_marks[name] = scores
    query_name = input()

    for key,value in student_marks.items():
        if key == query_name:
            average = sum(value)/3
            print(f"{average:.2f}")


def others_nested_list():
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    grades = [lis[1] for lis in students]
    grades = list(set(grades))
    grades.sort()

    runnerup = [lis for lis in students if grades[1] == lis[1]]
    runnerup = [lis[0] for lis in runnerup]
    runnerup.sort()

    for name in runnerup:
        print(name)


def sb_nested_list():
    students = []
    runnerups = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [score,name]
        students.append(student)

    students = sorted(students)
    
    for student in list(set(map(tuple,students))):
        if student[0] == students[1][0]:
            runnerups.append(student[1])

    for student in runnerups:
        print(student)


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



