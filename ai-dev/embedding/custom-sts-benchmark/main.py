# from sentence_transformers import SentenceTransformer
# from numpy import dot
# from numpy.linalg import norm
import json

# TODO - integrate dataset outputs to the script

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
    # embedding_model = SentenceTransformer(model)
    if level == "simple":
        dataset = examples()["simple"]
        for data in dataset:
            first_word = list(data.values())[0][0]
            second_word = list(data.values())[0][1]
            print(f"Model Name: {model}")
            print(f"First Word: {first_word}")
            print(f"Second Word: {second_word}")
            print(f"Cosine Similarity: 0.75\n")


def global_model_tester():
    dataset = models()
    for model in dataset["global-models"]:
        tester("simple", model)


def main():
    global_model_tester()


if __name__ == "__main__":
    main()
