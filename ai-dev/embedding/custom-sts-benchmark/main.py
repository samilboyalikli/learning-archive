# from sentence_transformers import SentenceTransformer
# from numpy import dot
# from numpy.linalg import norm
import json

result = {}


def examples():
    with open("turkish-dataset.json", "r", encoding='utf-8') as file:
        return json.load(file)


def models():
    with open("model-list.json", "r", encoding='utf-8') as file:
        return json.load(file)


def cosine_similarity(model, first_word, second_word):
    # embedding_model = SentenceTransformer(model)
    # e1 = model.encode(first_text)
    # e2 = model.encode(second_text)
    # similarity = dot(e1, e2)/(norm(e1)*norm(e2))
    # print(similarity)
    return 0.75


def tester(level, model):
    if level == "simple":
        dataset = examples()["simple"]
        for data in dataset:
            first_word = list(data.values())[0][0]
            second_word = list(data.values())[0][1]
            result_dictionary = {
                "Cosine Similarity": cosine_similarity(model, first_word, second_word),
                "First Word": first_word,
                "Second Word": second_word
            }
            result.setdefault(model, []).append(result_dictionary)


def global_model_tester():
    dataset = models()
    for model in dataset["global-models"]:
        tester("simple", model)
    for model in dataset["turkish-models"]:
        tester("simple", model)


def main():
    global_model_tester()
    with open("output.json", "w", encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
