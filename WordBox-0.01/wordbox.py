import json
import random

file_path = "dataset.json"
with open(file_path, "r") as file:
    dataset = json.load(file)

a1 = dataset.get("A1", {})
a = a1.get("A", {})

new_word = {
    "card_id": "",
    "card_name": "",
    "card_opposite": "",
    "card_opposite2": "",
    "card_opposite3": "",
    "card_type": "",
    "card_level": "",
    "card_time": ""
}

random_word = random.choice(a)
while random_word["card_type"] == "Daily":
    word = random_word.get("card_name", "")
    opposite = random_word.get("card_opposite", "")
    print(word)
    if input("Answer: ") == opposite:
        print("True")
        random_word["card_type"] = "Weekly"
    else: print(f"False. Answer was: {opposite}")
