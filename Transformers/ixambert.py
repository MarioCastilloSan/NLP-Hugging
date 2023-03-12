from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
# To load the model and tokenizer
modelQ = AutoModelForQuestionAnswering.from_pretrained("MarcBrun/ixambert-finetuned-squad-eu-en")
tokenizer = AutoTokenizer.from_pretrained("MarcBrun/ixambert-finetuned-squad-eu-en")


# To get predictions
context = "El Tajo es el río más largo de la península ibérica, a la que atraviesa en su parte central, siguiendo un rumbo este-oeste, con una leve inclinación hacia el suroeste, que se acentúa cuando llega a Portugal, donde recibe el nombre de Tejo. Nace en los montes Universales, en la sierra de Albarracín, sobre la rama occidental del sistema Ibérico y, después de recorrer 1007 km, llega al océano Atlántico en la ciudad de Lisboa. En su desembocadura forma el estuario del mar de la Paja, en el que vierte un caudal medio de 456 m³/s. En sus primeros 816 km atraviesa España, donde discurre por cuatro comunidades autónomas (Aragón, Castilla-La Mancha, Madrid y Extremadura) y un total de seis provincias (Teruel, Guadalajara, Cuenca, Madrid, Toledo y Cáceres)."
question = "¿Por qué provincias pasa el Tajo?"
def qaSP(qspvalue :str,cspvalue:str )->str:
    qa = pipeline("question-answering", model=modelQ, tokenizer=modelQ)
    pred = qa(question=qspvalue,context=cspvalue)
    return pred['answer']

print(qaSP(question,context))






