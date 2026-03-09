from sentence_transformers import SentenceTransformer
from numpy import dot
from numpy.linalg import norm
from huggingface_hub import model_info
from huggingface_hub.utils import RepositoryNotFoundError
import json
import os

os.environ["HF_TOKEN"] = "enter the token"
result = {"global-models": {}, "turkish-models": {}}
TESTTYPE = "d"
LEVEL = "expert"
DATAFILE = f"datasets/{TESTTYPE}-law-dataset.json"
SCOREFILE = f"law-test/{TESTTYPE}-law-score-{LEVEL}.json"
OUTPUTFILE = f"law-test/{TESTTYPE}-law-output-{LEVEL}.json"


def model_check(model_name: str) -> SentenceTransformer | None:
        try:
            model_info(model_name)
            print(f"[INFO] ✓ Model yükleniyor: {model_name}")
            return SentenceTransformer(model_name)
        except RepositoryNotFoundError:
            print(f"[INFO] ✗ Atlandı: {model_name}")


def examples():
    with open(DATAFILE, "r", encoding='utf-8') as file:
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


def tester(model_flag, model_name, model):
    dataset = examples()[LEVEL]
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
        model = model_check(model_name)
        if model is not None:
            tester("g", model_name, model)
    for model_name in dataset["turkish-models"]:
        model = model_check(model_name)
        if model is not None:
            tester("t", model_name, model)


def score():
    with open(OUTPUTFILE, "r", encoding='utf-8') as file:
        output = json.load(file)
    new_mo = []
    for model_type, model_results in output.items():
        mo = {model_type: []}
        for model_name, results in model_results.items():
            similarities = []
            for result in results:
                similarities.append(result["Cosine Similarity"])
            sts_score = sum(similarities)/len(similarities)
            mo[model_type].append((model_name, sts_score))
        if TESTTYPE == "s":
            new_mo.extend([
                {
                    "MODEL TYPE": key,
                    "AVERAGE SCORE": sum(x[1] for x in value)/len(value),
                    "MODEL RESULTS": sorted(value, key=lambda x: x[1], reverse=True)
                }
                for key, value in mo.items()
            ])
        else: 
            new_mo.extend([
                {
                    "MODEL TYPE": key,
                    "AVERAGE SCORE": sum(x[1] for x in value)/len(value),
                    "MODEL RESULTS": sorted(value, key=lambda x: x[1], reverse=False)
                }
                for key, value in mo.items()
            ]) 
    with open(SCOREFILE, "w", encoding='utf-8') as file:
        json.dump(new_mo, file, ensure_ascii=False, indent=4)


def main():
    global_model_tester()
    with open(OUTPUTFILE, "w", encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
    score()


if __name__ == "__main__":
    main()
