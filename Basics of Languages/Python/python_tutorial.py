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


def bmi_index():
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    bmi = weight/(height**2)
    print(f"BMI: {round(bmi,2)}")
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25.0:
        print("Normal Weight")
    elif 25.0 <= bmi < 30.0:
        print("Overweight")
    elif 30.0 <= bmi < 40.0:
        print("Obese")
    elif 40.0 <= bmi:
        print("Morbidly Obese")
    else: print("There is a problem.")


def while_loop():
    i = 1
    while i <= 10:
        print("*" * i)
        i = i+1
    while i <= 10:
        print(i)


def lists():
    items = ["a","b","c","d","e"]
    print(items)
    print(items[0])
    print(items[-1])
    print(items[-2])
    top_two = items[0:2]
    print(top_two)


def most_used_list_methods():
    items = ["a","b","c","d","e"]
    print(items)
    items.append("f")
    print("items.append('f') - ", items)
    items.insert(0, "g")
    print("items.insert(0,'g') - ", items)
    items.remove("f")
    print("items.remove('f') - ", items)
    print("len(items) - ", len(items))
    print("'d' in items - ", "d" in items)
    items.clear()
    print("items.clear() - ", items)   


def for_loops():
    items = [1,2,3,4,5]
    for item in items:
        print(item)
    i = 0
    while i<len(items):
        print(items[i])
        i += 1


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
    #bmi_index()
    #while_loop()
    #lists()
    #most_used_list_methods()
    #for_loops()


