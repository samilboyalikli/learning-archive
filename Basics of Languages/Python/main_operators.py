# 1. equivalent
# 2. noneequivalent
# 3. if block
# 4. negation
# 5. conjunction
# 6. disjunction

# 1. equal operator is "=":
a = 3
b = 3

# 2. not equal operator is "!=":
# 3. when we use equality in an if block, we must use "=="
if a == b:
    print("True")
elif a != b:
    print("False")
else:
    print("wtf!?")

# 4. negation
a = True
b = not a
print(b)
# b will be False

# 5. conjunction
x = True
y = True
if x and y:
    print("all values positive")

# 6. disjunction
t = True
z = False
if t or z:
    print("all values not positive")

