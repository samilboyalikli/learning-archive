octal_mods = []
hexadecimal_mods = []
binary_mods = []

# OCTAL PROCESSES

def octal_divide(x):
    quotient = x/8
    mod = x%8
    return quotient, mod


def octal_non_zero_quotient(quotient):
    result = octal_divide(quotient)
    octal_mods.append(result[1])
    return int(result[0])


def octal_main(number):
    check_quotient = octal_non_zero_quotient(number)
    while check_quotient > 0:
        number = check_quotient
        check_quotient = octal_non_zero_quotient(number)

# HEXADECIMAL PROCESSES

def hexadecimal_divide(x):
    quotient = x/16
    mod = x%16
    return quotient, mod


def hexadecimal_non_zero_quotient(quotient):
    result = hexadecimal_divide(quotient)
    hexadecimal_mods.append(result[1])
    return int(result[0])


def hexadecimal_main(number):
    check_quotient = hexadecimal_non_zero_quotient(number)
    while check_quotient > 0:
        number = check_quotient
        check_quotient = hexadecimal_non_zero_quotient(number)


def convert_to_hex_char(value):
    hex_chars = "0123456789ABCDEF"
    return hex_chars[value]

# BINARY PROCESSES

def binary_divide(x):
    quotient = x/2
    mod = x%2
    return quotient, mod


def binary_non_zero_quotient(quotient):
    result = binary_divide(quotient)
    binary_mods.append(result[1])
    return int(result[0])


def binary_main(number):
    check_quotient = binary_non_zero_quotient(number)
    while check_quotient > 0:
        number = check_quotient
        check_quotient = binary_non_zero_quotient(number)

# CONVERTING

def print_formatted(n):
    for i in range(1,n+1):
        global binary_mods
        global octal_mods
        global hexadecimal_mods
        binary_main(i)  
        octal_main(i)  
        hexadecimal_main(i)
        hexadecimal_mods = [convert_to_hex_char(i) for i in hexadecimal_mods]
        binary_result = ''.join(map(str,binary_mods[::-1]))
        octal_result = ''.join(map(str,octal_mods[::-1])) 
        hexadecimal_result = ''.join(map(str,hexadecimal_mods[::-1]))
        print(i,octal_result,hexadecimal_result,binary_result)
        binary_mods = []
        octal_mods = []
        hexadecimal_mods = []

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
