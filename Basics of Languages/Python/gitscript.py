# TODO
#   1. Setting date part.
#   2. Writing on powershell.
#   3. Main configurations.

def inputs():
    file_name = input("Write your file name with path: ")
    commit_message = input("Write your commit: ")
    date = input("Write date which want to push: ")
    return file_name, commit_message, date


def push(file_name):
    result = print(f"git add {file_name}")
    return result 


def commit(commit_message):
    result = print(f"git commit -m {commit_message}")
    return result


def main():
    file_name, commit_message, date = inputs()
    push(file_name)
    commit(commit_message)
    print(f"Date: {date}")


if __name__ == "__main__":
    main()
      

