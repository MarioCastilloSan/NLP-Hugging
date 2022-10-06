from transformers import AutoTokenizer,AutoModelWithLMHead
model = AutoModelWithLMHead.from_pretrained("T5Files")
tokenizer = AutoTokenizer.from_pretrained("T5Files")

#To download this model
#tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")
#model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-question-generation-ap")

#To save it once you download it
#tokenizer.save_pretrained("T5Files")
#model.save_pretrained("T5Files")

def get_question(answer, context, max_length=64):
  input_text = "answer: %s  context: %s </s>" % (answer, context)
  features = tokenizer([input_text], return_tensors='pt')

  output = model.generate(input_ids=features['input_ids'], 
               attention_mask=features['attention_mask'],
               max_length=max_length)

  return tokenizer.decode(output[0])

context = "Manuel has created RuPERTa-base with the support of HF-Transformers and Google"
answer = "Manuel"

print(get_question(answer, context))
