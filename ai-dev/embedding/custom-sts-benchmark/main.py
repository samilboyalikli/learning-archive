# from sentence_transformers import SentenceTransformer
# from numpy import dot
# from numpy.linalg import norm
import json

result = {
    "global-models": {},
    "turkish-models": {}
}


def examples():
    with open("turkish-dataset.json", "r", encoding='utf-8') as file:
        return json.load(file)


def models():
    with open("model-list.json", "r", encoding='utf-8') as file:
        return json.load(file)


def cosine_similarity(model, first_word, second_word):
    e1 = model.encode(first_word)
    e2 = model.encode(second_word)
    similarity = dot(e1, e2)/(norm(e1)*norm(e2))
    print(f"[INFO] Similarity: {similarity}\n")
    return similarity.item()


def tester(model_flag, level, model_name, model):
    if level == "simple":
        dataset = examples()["simple"]
        for data in dataset:
            first_word = list(data.values())[0][0]
            second_word = list(data.values())[0][1]
            print(f"[INFO] Model: {model_name}")
            result_dictionary = {
                "Cosine Similarity": cosine_similarity(model, first_word, second_word),
                "First Word": first_word,
                "Second Word": second_word
            }
            if model_flag == "g":
                result["global-models"].setdefault(model_name, []).append(result_dictionary)
            else: 
                result["turkish-models"].setdefault(model_name, []).append(result_dictionary)


def global_model_tester():
    dataset = models()
    for model_name in dataset["global-models"]:
        model = SentenceTransformer(model_name)
        tester("g", "simple", model_name, model)
    for model_name in dataset["turkish-models"]:
        model = SentenceTransformer(model_name)
        tester("t", "simple", model_name, model)


def score():
    with open("output.json", "r", encoding='utf-8') as file:
        output = json.load(file)
    for model_type, model_results in output.items():
        mo = {model_type: []}
        for model_name, results in model_results.items():
            similarities = []
            for result in results:
                similarities.append(result["Cosine Similarity"])
            sts_score = sum(similarities)/len(similarities)
            mo[model_type].append((model_name, sts_score))
        mo = {
            key: sorted(value, key=lambda x: x[1], reverse=True)
            for key, value in mo.items()
        }
        print(mo)


def main():
    global_model_tester()
    with open("output.json", "w", encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # main()
    score()
