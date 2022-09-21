import argparse
parser= argparse.ArgumentParser()
parser.add_argument('qvalue', help="Question", type=str)
parser.add_argument('cvalue', help="Context", type=str)
args=parser.parse_args()



from transformers import *

# Important!: By now the QA pipeline is not compatible with fast tokenizer, but they are working on it. So that pass the object to the tokenizer {"use_fast": False} as in the following example:

nlp = pipeline(
    'question-answering', 
    model='mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',
    tokenizer=(
        'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',  
        {"use_fast": False}
    )
)

nlp(
    {
        'question': '¿Para qué lenguaje está trabajando?',
        'context': 'Manuel Romero está colaborando activamente con huggingface/transformers ' +
                    'para traer el poder de las últimas técnicas de procesamiento de lenguaje natural al idioma español'
    }
)