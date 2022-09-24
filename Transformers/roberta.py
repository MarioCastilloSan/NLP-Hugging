from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
model_name = "deepset/roberta-base-squad2"
# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
#base question 'Why is model conversion important?'
#base context 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
def qa(qvalue,cvalue):
    QA_input = {
        'question': qvalue,
        'context': cvalue
    }
    res = nlp(QA_input) 
    return res



