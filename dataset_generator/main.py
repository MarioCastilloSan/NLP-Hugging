import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

cuestionarios = [
    "https://psicologiaymente.com/miscelanea/preguntas-y-respuestas",
    "https://psicologiaymente.com/cultura/preguntas-cultura-general",
    "https://medicoplus.com/ciencia/preguntas-cultura-general",
    "https://www.cosmopolitan.com/es/consejos-planes/familia-amigos/a40706432/200-preguntas-de-cultura-general-y-su-respuesta/",
]
url = cuestionarios[0]
req = requests.get(url)


def unir(lista):
    return " ".join(lista)

def psicologiaymente(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    contenedor = soup.find("div", {"id": "article-content-container"})
    h3 = contenedor.find_all("h3")
    p = contenedor.find_all("p")

    for q, r in zip(h3, p[3:]):
        print(q.text)
        print(r.text)
        print("")


psicologiaymente(cuestionarios[1])
