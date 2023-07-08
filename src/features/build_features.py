import torch
from transformers import AutoTokenizer, AutoModel
from numpy import vectorize
import pandas as pd


def embed_bert_cls(text, model, tokenizer):
    t = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**{k: v.to(model.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings[0].cpu().numpy()


def bert_embeding(x, model, tokenizer):
    return embed_bert_cls(x, model, tokenizer).reshape(1, 312)[0, 57]


def bert(df):  # добавляет в датасет emb57

    tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2")
    model = AutoModel.from_pretrained("cointegrated/rubert-tiny2")
    # model.cuda()  # uncomment it if you have a GPU

    df['emb57'] = vectorize(bert_embeding)(df['text'], model, tokenizer)
    df = df.drop('text', axis=1)
    return df



