import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


genreDf = pd.read_excel('datasetCiclosTiempos.xlsx')
#genreDf=df.drop_duplicates(subset=['CantidadPalabras','Tiempo'], keep='last')
#genreDf.to_excel('genreDf.xlsx',index=False)
#genreDf = pd.read_excel('genreDf.xlsx')


###Generos

#########Drama
promswG5=[]
promswG10=[]
promswG15=[]

dfSSG=genreDf[(genreDf['Solapamiento']==False) & (genreDf['Secciones']==64 )&(genreDf['Genero']=='Drama')]
top_5SSG = dfSSG.sort_values('ScoreA', ascending=False).head(5)
top_10SSG = dfSSG.sort_values('ScoreA', ascending=False).head(10)
top_15SSG = dfSSG.sort_values('ScoreA', ascending=False).head(15)
array_top_5SSG = top_5SSG['ScoreA'].tolist()
array_top_10SSG = top_10SSG['ScoreA'].tolist()
array_top_15SSG = top_15SSG['ScoreA'].tolist()
promswG5.append(np.mean(array_top_5SSG))
promswG10.append(np.mean(array_top_10SSG))
promswG15.append(np.mean(array_top_15SSG))

#########Lírica
promswL5=[]
promswL10=[]
promswL15=[]
dfSSL=genreDf[(genreDf['Solapamiento']==False) & (genreDf['Secciones']==64) &(genreDf['Genero']=='Lírica')]
top_5SSL = dfSSL.sort_values('ScoreA', ascending=False).head(5)
top_10SSL = dfSSL.sort_values('ScoreA', ascending=False).head(10)
top_15SSL = dfSSL.sort_values('ScoreA', ascending=False).head(15)
array_top_5SSL = top_5SSL['ScoreA'].tolist()
array_top_10SSL = top_10SSL['ScoreA'].tolist()
array_top_15SSL = top_15SSL['ScoreA'].tolist()
promswL5.append(np.mean(array_top_5SSL))
promswL10.append(np.mean(array_top_10SSL))
promswL15.append(np.mean(array_top_15SSL))

########## Narrativa
promswN5=[]
promswN10=[]
promswN15=[]
dfSSN=genreDf[(genreDf['Solapamiento']==False) & (genreDf['Secciones']==64) &(genreDf['Genero']=='Narrativa')]
dfSSN=dfSSN[(dfSSN['NombreTexto']=='El hijo del elefante.pdf') +  (dfSSN['NombreTexto']=='La sirenita.pdf')+ (dfSSN['NombreTexto']=='Tom Sawyer.pdf')+ (dfSSN['NombreTexto']=='El patito feo.pdf')+ (dfSSN['NombreTexto']=='Juan Darien.pdf')]
top_5SSN = dfSSN.sort_values('ScoreA', ascending=False).head(5)
top_10SSN = dfSSN.sort_values('ScoreA', ascending=False).head(10)
top_15SSN = dfSSN.sort_values('ScoreA', ascending=False).head(15)
array_top_5SSN = top_5SSN['ScoreA'].tolist()
array_top_10SSN = top_10SSN['ScoreA'].tolist()
array_top_15SSN = top_15SSN['ScoreA'].tolist()
promswN5.append(np.mean(array_top_5SSN))
promswN10.append(np.mean(array_top_10SSN))
promswN15.append(np.mean(array_top_15SSN))



def graphGenre(y1:list,y2:list,y3:list):
    plt.figure(figsize=(12, 8))
    plt.ylabel('Score',fontsize=15);
    plt.ylim(0.10, 1)   
    #64
    genre = ['Drama','Lyric','Narrative']
    counts=[y1[0],y2[0],y3[0]]
    bar_colors = ['tab:red', 'tab:blue',  'tab:green']
    plt.bar(genre, counts, color=bar_colors)
    plt.tick_params(axis="both", labelsize=15)
    plt.show()


graphGenre(promswG15,promswL15,promswN15)

