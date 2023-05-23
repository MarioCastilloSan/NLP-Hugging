import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('datasetCiclos.xlsx')

### 1ro basico
xcs=df[(df['Nivel']=='1ro basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss=df[(df['Nivel']=='1ro basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean=xcs['ScoreA'].mean()
xssMean=xss['ScoreA'].mean()

### 2do basico
xcs2=df[(df['Nivel']=='2do basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss2=df[(df['Nivel']=='2do basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean2=xcs2['ScoreA'].mean()
xssMean2=xss2['ScoreA'].mean()

### 3ro basico
xcs3=df[(df['Nivel']=='3ro basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss3=df[(df['Nivel']=='3ro basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean3=xcs3['ScoreA'].mean()
xssMean3=xss3['ScoreA'].mean()

### 4to basico
xcs4=df[(df['Nivel']=='4to basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss4=df[(df['Nivel']=='4to basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean4=xcs4['ScoreA'].mean()
xssMean4=xss4['ScoreA'].mean()

### 5to basico
xcs5=df[(df['Nivel']=='5to basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss5=df[(df['Nivel']=='5to basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean5=xcs5['ScoreA'].mean()
xssMean5=xss5['ScoreA'].mean()

### 6to basico
xcs6=df[(df['Nivel']=='6to basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xss6=df[(df['Nivel']=='6to basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMean6=xcs6['ScoreA'].mean()
xssMean6=xss6['ScoreA'].mean()



## All years without overlap mean
xcsAll=df[(df['Nivel']=='4to basico') & (df['Solapamiento']==True)& (df['Secciones']==64)]
xssAll=df[(df['Nivel']=='4to basico') & (df['Solapamiento']==False) &  (df['Secciones']==64)]
xcsMeanAll=xcsAll['ScoreA'].mean()
xssMeanAll=xssAll['ScoreA'].mean()





top=15


proms=[]
###Niveles Educacioneles Con Solapamiento
sections=[64,128,192,256]
for i in sections:
    df1ro=df[(df['Nivel']=='1ro basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15 = df1ro.sort_values('ScoreA', ascending=False).head(top)
    array_top_15 = top_15['ScoreA'].tolist()

    df2do=df[(df['Nivel']=='2do basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_2do = df2do.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_2do = top_15_2do['ScoreA'].tolist()

    df3ro=df[(df['Nivel']=='3ro basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_3ro = df3ro.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_3ro = top_15_3ro['ScoreA'].tolist()

    df4to=df[(df['Nivel']=='4to basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_4to = df4to.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_4to = top_15_4to['ScoreA'].tolist()

    df5to=df[(df['Nivel']=='5to basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_5to = df5to.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_5to = top_15_5to['ScoreA'].tolist()

    df6to=df[(df['Nivel']=='6to basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_6to = df6to.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_6to = top_15_6to['ScoreA'].tolist()

    df7mo=df[(df['Nivel']=='7tmo basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_7mo = df7mo.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_7mo = top_15_7mo['ScoreA'].tolist()

    df8vo=df[(df['Nivel']=='8vo basico')& (df['Solapamiento']==True)& (df['Secciones']==i)]
    top_15_8vo = df8vo.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_8vo = top_15_8vo['ScoreA'].tolist()

    promediosConSolapamiento=[np.mean(array_top_15),np.mean(array_top_15_2do),np.mean(array_top_15_3ro),np.mean(array_top_15_4to),np.mean(array_top_15_5to),np.mean(array_top_15_6to),np.mean(array_top_15_7mo),np.mean(array_top_15_8vo)]
    proms.append(promediosConSolapamiento)
    




promsw=[]
###Niveles Educacioneles Sin Solapamiento
for i in sections:
    df1roSS=df[(df['Nivel']=='1ro basico')& (df['Solapamiento']==False) & (df['Secciones']==i)]
    top_15SS = df1roSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15SS = top_15SS['ScoreA'].tolist()

    df2doSS=df[(df['Nivel']=='2do basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_2doSS = df2doSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_2doSS = top_15_2doSS['ScoreA'].tolist()

    df3roSS=df[(df['Nivel']=='3ro basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_3roSS = df3roSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_3roSS = top_15_3roSS['ScoreA'].tolist()

    df4toSS=df[(df['Nivel']=='4to basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_4toSS = df4toSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_4toSS = top_15_4toSS['ScoreA'].tolist()

    df5toSS=df[(df['Nivel']=='5to basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_5toSS = df5toSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_5toSS = top_15_5toSS['ScoreA'].tolist()

    df6toSS=df[(df['Nivel']=='6to basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_6toSS = df6toSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_6toSS = top_15_6toSS['ScoreA'].tolist()

    df7moSS=df[(df['Nivel']=='7tmo basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_7moSS = df7moSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_7moSS = top_15_7moSS['ScoreA'].tolist()


    df8voSS=df[(df['Nivel']=='8vo basico')& (df['Solapamiento']==False)& (df['Secciones']==i)]
    top_15_8voSS = df8voSS.sort_values('ScoreA', ascending=False).head(top)
    array_top_15_8voSS = top_15_8voSS['ScoreA'].tolist()

    promediosSinSolapamiento=[np.mean(array_top_15SS),np.mean(array_top_15_2doSS),np.mean(array_top_15_3roSS),np.mean(array_top_15_4toSS),np.mean(array_top_15_5toSS),np.mean(array_top_15_6toSS),np.mean(array_top_15_7moSS),np.mean(array_top_15_8voSS)]
    promsw.append(promediosSinSolapamiento)




def graphEducationalLevels(x:list,y1:list,y2:list,section:int,top:int):
    plt.figure(figsize=(12, 8))
    plt.xlabel('Levels',fontsize=15);
    plt.ylabel('Score',fontsize=15);
    plt.ylim(0, 1)   
    #64
    plt.plot(x, y1[0], 's--', color='red',label=f"064_O")
    plt.plot(x, y2[0], 'o-',color='blue', label=f"064_W")
    #128
    plt.plot(x, y1[1], 's--', color='gray',label=f"128_O",)
    plt.plot(x, y2[1], 'o-',color='black', label=f"128_W")
    #192
    plt.plot(x, y1[2], 's--', color='cyan',label=f"192_O",)
    plt.plot(x, y2[2], 'o-',color='orange', label=f"192_W")
    #256
    plt.plot(x, y1[3], 's--', color='darkgreen',label=f"256_O",)
    plt.plot(x, y2[3], 'o-',color='purple', label=f"256_W")
    plt.legend(fontsize=15)
    plt.tick_params(axis="both", labelsize=15)
    plt.show()

x=['1','2','3','4','5','6','7','8']
#graphEducationalLevels(x,proms,promsw,secciones,top)





xG=[64,128,192,256]

promsG5=[]
promsG10=[]
promsG15=[]
###Niveles Educacioneles Con Solapamiento
sections=[64,128,192,256]
for i in sections:
    dfGeneral=df[(df['Solapamiento']==True)& (df['Secciones']==i)]
    top_5G = dfGeneral.sort_values('ScoreA', ascending=False).head(5)
    top_10G = dfGeneral.sort_values('ScoreA', ascending=False).head(10)
    top_15G = dfGeneral.sort_values('ScoreA', ascending=False).head(15)
    array_top_5G = top_5G['ScoreA'].tolist()
    array_top_10G = top_10G['ScoreA'].tolist()
    array_top_15G = top_15G['ScoreA'].tolist() 
    promsG5.append(np.mean(array_top_5G))
    promsG10.append(np.mean(array_top_10G))
    promsG15.append(np.mean(array_top_15G))
    
promswG5=[]
promswG10=[]
promswG15=[]
###Niveles Educacioneles Generales Sin Solapamiento
for i in sections:
    dfSSG=df[(df['Solapamiento']==False) & (df['Secciones']==i)]
    top_5SSG = dfSSG.sort_values('ScoreA', ascending=False).head(5)
    top_10SSG = dfSSG.sort_values('ScoreA', ascending=False).head(10)
    top_15SSG = dfSSG.sort_values('ScoreA', ascending=False).head(15)
    array_top_5SSG = top_5SSG['ScoreA'].tolist()
    array_top_10SSG = top_10SSG['ScoreA'].tolist()
    array_top_15SSG = top_15SSG['ScoreA'].tolist()
    promswG5.append(np.mean(array_top_5SSG))
    promswG10.append(np.mean(array_top_10SSG))
    promswG15.append(np.mean(array_top_15SSG))

def graphEducationalLevelsGeneral(x:list,y1:list,y2:list,y3:list,y4:list,y5:list,y6:list):
    plt.figure(figsize=(12, 8))
    plt.xlabel('Tokens',fontsize=15);
    plt.ylabel('Score',fontsize=15);
    #plt.ylim(0.0, 1.0)   
    #64

    plt.plot(x, y3, 's--', color='red',label=f"O_top(10)")
    plt.plot(x, y4, 'o-',color='blue', label=f"W_top(10)")
    plt.tick_params(axis="both", labelsize=15)
    plt.legend(fontsize=15)
    plt.xticks(xG)
    plt.show()

graphEducationalLevelsGeneral(xG,promsG5,promswG5,promsG10,promswG10,promsG15,promswG15)
print(promsG5,promswG5,xG)
