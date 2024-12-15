import json
import random
from datetime import datetime

file_path = "dataset.json"
with open(file_path, "r") as file:
    dataset = json.load(file)



def saving():
    with open(file_path, "w") as file:
        json.dump(dataset, file, indent=4)


def true_answer(x):
    if x["card_type"] == "Daily":
        x["card_type"] = "Weekly"
        saving()
    else:
        x["card_type"] = "Monthly"
        saving()


def wrong_answer(x):
    if x["card_type"] == "Monthly":
        x["card_type"] = "Weekly"
        saving()
    else:
        x["card_type"] = "Daily"
        saving()


user_input = input("\nfor testing press 0\nfor add new word press 1\n\n")
if user_input == "0":
    user_input_0 = input("\nfor wordbox press 0\nfor your wordbox press 1\n\n")
    if user_input_0 == "0":
        a1 = dataset.get("A1", {})
        a = a1.get("A", {})
        random_word = random.choice(a)
        while random_word["card_type"] == "Daily":
            word = random_word.get("card_name", "")
            opposite = random_word.get("card_opposite", "")
            print(f"\n{word}")
            if input("Answer: ") == opposite:
                print("True")
                true_answer(random_word)
            else:
                print(f"\nFalse\nAnswer was: {opposite}\n")
                wrong_answer(random_word)
    elif user_input_0 == "1":
        while True:
            daily_word = [word for word in dataset.get("new_words", []) if word.get("card_type") == "Daily"]
            random_word = random.choice(daily_word)
            word = random_word.get("card_name", "")
            opposite = random_word.get("card_opposite", "")
            print(f"\n{word}")
            if input("Answer: ") == opposite:
                print("\nTrue\n")
                true_answer(random_word)
            else: 
                print(f"\nFalse\nAnswer was: {opposite}\n")
                wrong_answer(random_word)
    else:
        print("\n\nPlease press 0 or 1\n\n\nWordBox")
elif user_input == "1": 
    while True:
        word_dict = {
            "card_id": "",
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
        new_word_list = list(dataset.values())[1]
        last_new_word = new_word_list[-1]
        word_dict["card_id"] = int(last_new_word["card_id"]) + 1
        print(word_dict)
        dataset["new_words"].append(word_dict)
        print("\nFor exit press 0\nFor adding other word press 1")
        if input() == '1':
            print("\nWordBox 0.01\n\n")
        else: 
            break
else:
    print("\n\nPlease press 0 or 1\n\n\nWordBox")
