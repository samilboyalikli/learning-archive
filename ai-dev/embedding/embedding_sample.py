import torch
from sentence_transformers import SentenceTransformer

print("Torch version: ", torch.__version__)
print("CUDA available: ", torch.cuda.is_available())
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Sentence-transformers is ready!")

text = "Hello World"
embedding = model.encode(text)

print(f"SHAPE: {embedding.shape}")
print(f"TYPE: {type(embedding)}")
print(f"SIZE (dtype): {embedding.dtype}")
print(f"SIZE (nbytes): {embedding.nbytes}")
print(f"OUTPUT: {embedding}")
