# from sentence_transformers import SentenceTransformer
# from numpy import dot
# from numpy.linalg import norm
import json

# TODO - write simple 2 global model and turkish model into the model-list.json
# TODO - open model names from model-list.json
# TODO - integrate dataset outputs to the script

# model = SentenceTransformer("all-miniLM-L6-v2")

# first_text = input("Enter first text please: ")
# second_text = input("Enter second text please: ")

# e1 = model.encode(first_text)
# e2 = model.encode(second_text)

# similarity = dot(e1, e2)/(norm(e1)*norm(e2))
# print(similarity)


def examples():
    with open("turkish-dataset.json", "r", encoding='utf-8') as file:
        return json.load(file)


def models():
    with open("model-list.json", "r", encoding='utf-8') as file:
        return json.load(file)


def tester(level, model):
    if level == "simple":
        dataset = examples()[""]
    pass


def main():
    words = examples()["simple"]
    for word in words:
        print(f"first word: {list(word.values())[0][0]}")
        print(f"second word: {list(word.values())[0][1]}\n")


if __name__ == "__main__":
    main()
