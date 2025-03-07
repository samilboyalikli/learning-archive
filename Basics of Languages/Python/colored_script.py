import time
import random


def step1():
    """We just see how work ANSI codes in this code block."""
    green = "\033[92m"
    red = "\033[91m"
    reset = "\033[0m"

    while True:
        print(f"{green}a{reset}")
        print(f"{red}b{reset}")
        time.sleep(0.5)


def step2():
    """We are modulizing ANSI codes in this code blocks."""
    greenColor = "\033[92m"
    redColor = "\033[91m"
    reset = "\033[0m"

    
    def green(value):
        return print(f"{greenColor}{value}{reset}")


    def red(value): 
        return print(f"{redColor}{value}{reset}")


    while True:
        green("a")
        red("b")
        time.sleep(0.5)


def step3():
    """We are adding a conditional function to ANSI code blocks."""
    greenColor = "\033[92m"
    redColor = "\033[91m"
    reset = "\033[0m"


    def green(value):
        return print(f"{greenColor}{value}{reset}")


    def red(value):
        return print(f"{redColor}{value}{reset}")


    def random_value():
        return random.randint(0,100)


    def checking(number):
        if (number>=0) and (number<=49):
            red(number)
        elif (number>=50) and (number<=100):
            green(number)
        else: print("Please check the random number.")


    while True:
        checking(random_value())
        time.sleep(1)


if __name__ == "__main__":
    step3()

