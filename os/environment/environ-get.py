import os

all_vars = os.environ

for key, value in list(all_vars.items()):
    print(f"{key}: {value}")
