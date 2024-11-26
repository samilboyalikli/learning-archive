import json
import random
from datetime import datetime

file_path = "dataset.json"
with open(file_path, "r") as file:
    dataset = json.load(file)

a1 = dataset.get("A1", {})
a = a1.get("A", {})

print(
"""
for training press 0
for add new word press 1
"""
)

if input() == "0":
    print(
    """
for wordbox press 0
for your wordbox press 1
    """
    )
    if input() == "0":
        a1 = dataset.get("A1", {})
        a = a1.get("A", {})
        random_word = random.choice(a)
        while random_word["card_type"] == "Daily":
            word = random_word.get("card_name", "")
            opposite = random_word.get("card_opposite", "")
            print(word)
            if input("Answer: ") == opposite:
                print("True")
                random_word["card_type"] = "Weekly"
            else: print(f"False. Answer was: {opposite}")
    else: 
        new_words = dataset.get("new_words", {})
        random_word = random.choice(new_words)
        while random_word["card_type"] == "Daily":
            word = random_word.get("card_name", "")
            opposite = random_word.get("card_opposite", "")
            print(word)
            if input("Answer: ") == opposite:
                print("True")
                random_word["card_type"] = "Weekly"
            else: print(f"False. Answer was: {opposite}")
else: 
    word_dict = {
        "card_name": "",
        "card_opposite": "",
        "card_type": "Daily",
        "card_level": "",
        "card_time": ""
    }
    new_word = input("word: ")
    new_opposite = input("meaning: ")
    new_card_level = input("level of the word: ")
    word_dict["card_name"] = new_word
    word_dict["card_opposite"] = new_opposite
    word_dict["card_level"] = new_card_level
    formatted_date = datetime.now().strftime("%d-%m-%Y")
    word_dict["card_time"] = formatted_date
    print(word_dict)


# with open(file_path, "w") as file:
#         json.dump(dataset, file, indent=4)


# new_word = {
#     "card_id": "",
#     "card_opposite2": "",
#     "card_opposite3": "",
# }

