import os

user_name = os.getenv('USER')

if user_name is None:
    user_name = os.getenv('USERNAME')

print(f"User Name Variable: {user_name}")
