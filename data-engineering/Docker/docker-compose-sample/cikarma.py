import random

def cikarma():
    a, b = random.randint(1, 100), random.randint(1, 100)
    print(f"Çıkarma: {a} - {b} = {a - b}")

if __name__ == "__main__":
    cikarma()

