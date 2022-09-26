import json
import pandas as pd
df=pd.read_json("datasets/xquad.es.json")

def qaSelection( question :int,context:int, )->str:
    q=df['data'][0]['paragraphs'][context]['context']
    c=df['data'][0]['paragraphs'][context]['qas'][question]['question']
    return q,c

print(qaSelection(0,2))