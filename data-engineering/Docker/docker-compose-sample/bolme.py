import random

def bolme():
    a, b = random.randint(1, 100), random.randint(1, 100)
    if b != 0:
        print(f"Bölme: {a} / {b} = {a / b:.2f}")
    else:
        print("Bölme: Bölüm sıfıra eşit olamaz!")

if __name__ == "__main__":
    bolme()

