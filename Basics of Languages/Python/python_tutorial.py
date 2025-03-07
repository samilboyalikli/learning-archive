"""The file includes basics of Python."""


def prints():
    print("Hello, world!")
    print(1+2)


def variables():
    name = "Samil"
    surname = "Boyalikli"
    age = 27
    return print(f"{name}\t{surname}\t{age}")


def receiving_input():
    name = input("What is your name?")
    print("Hello "+name+".")


def data_type_conversion():
    year = input("What year were you born?")
    age = 2025 - int(year)
    return print(age)


def string_operations():
    word = "Python language is so easy."
    print(word.upper())
    print(word.lower())
    print(word.find("P"))
    print(word.find("Python"))
    print(word.replace("Python","Golang"))
    print("Python" in word)
    print("Golang" in word)


def arithmetic_operators():
    print(10+3)
    print(10-3)
    print(10*3)
    print(10/3)
    print(10//3)
    print(10%3)
    print(10**3)
    number = 10
    print(number)
    number += 3
    print(number)


def comparison_operators():
    print("x=10>3")
    x=10>3
    print(10>3)
    print(10<3)
    print(10>=3)
    print(10<=3)
    print(10==10)
    print(10!=10)


def logical_operators():
    value = 10
    print(value>50 and value<100)
    print(value>50 or value<100)
    print(not (value<50))


def conditional_statements():
    grade = int(input("What is your grade?"))
    if grade >= 50:
        print("Congratulations. You succeeded.")
    elif grade <= 50:
        print("Unfortunately. You must try again.")
    else: print("There is no grade like you wrote.")


def keywords():
    print(
    """
    1. and
    2. break
    3. elif
    4. for
    5. in
    6. not
    7. True
    8. as
    9. class
    10. else
    11. from
    12. is
    13. or
    14. try,
    15. assert
    16. continue
    17. except
    18. global
    19. lambda
    20. pass
    21. while
    22. async
    23. def
    24. False,
    25. if
    26. None
    27. raise
    28. with
    29. await
    30. del
    31. finally
    32. import
    33. nonlocal
    34. return
    35. yield.
    """)


if __name__ == "__main__":
    #keywords()
    #prints()
    #variables()
    #receiving_input()
    #data_type_conversion()
    #string_operations()
    #arithmetic_operators()
    #comparison_operators()
    #logical_operators()
    #conditional_statements()



