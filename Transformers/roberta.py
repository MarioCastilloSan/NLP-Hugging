import argparse
parser= argparse.ArgumentParser()
parser.add_argument('qvalue', help="Question", type=str)
parser.add_argument('cvalue', help="Context", type=str)
args=parser.parse_args()



from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
#base question 'Why is model conversion important?'
#base context 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
QA_input = {
    'question': args.qvalue,
    'context': args.cvalue
}
res = nlp(QA_input)
print(res)