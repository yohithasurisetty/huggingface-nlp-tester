import torch
from transformers import pipeline

def load_model(model_name):
    return pipeline("sentiment-analysis", model=model_name)

def predict(model, texts):
    raw_preds = model(texts)
    return [1 if p['label'].upper().startswith("POS") else 0 for p in raw_preds]
