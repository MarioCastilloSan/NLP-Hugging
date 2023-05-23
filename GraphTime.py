import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#df = pd.read_excel('datasetCiclosTiempos.xlsx')
#finalTime=df.drop_duplicates(subset=['CantidadPalabras','Tiempo'], keep='last')
#finalTime.to_excel('timeData.xlsx',index=False)
finalTime = pd.read_excel('timeData.xlsx')


#1
sSolapamiento1=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==1)]
tiempoSinSolapado1=sSolapamiento1['Tiempo'].tolist()
palabrasSinSolapado1=sSolapamiento1['CantidadPalabras'].tolist()


#2
sSolapamiento2=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==2)]
tiempoSinSolapado2=sSolapamiento2['Tiempo'].tolist()
palabrasSinSolapado2=sSolapamiento2['CantidadPalabras'].tolist()

#3
sSolapamiento3=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==3)]
tiempoSinSolapado3=sSolapamiento3['Tiempo'].tolist()
palabrasSinSolapado3=sSolapamiento3['CantidadPalabras'].tolist()

#4
sSolapamiento4=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==4)]
tiempoSinSolapado4=sSolapamiento4['Tiempo'].tolist()
palabrasSinSolapado4=sSolapamiento4['CantidadPalabras'].tolist()

#5
sSolapamiento5=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==5)]
tiempoSinSolapado5=sSolapamiento5['Tiempo'].tolist()
palabrasSinSolapado5=sSolapamiento5['CantidadPalabras'].tolist()

#6
sSolapamiento6=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==6)]
tiempoSinSolapado6=sSolapamiento6['Tiempo'].tolist()
palabrasSinSolapado6=sSolapamiento6['CantidadPalabras'].tolist()

#7
sSolapamiento7=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==7)]
tiempoSinSolapado7=sSolapamiento7['Tiempo'].tolist()
palabrasSinSolapado7=sSolapamiento7['CantidadPalabras'].tolist()

#8
sSolapamiento8=finalTime[(finalTime['Solapamiento']==False)&(finalTime['Nivel']==8)]
tiempoSinSolapado8=sSolapamiento8['Tiempo'].tolist()
palabrasSinSolapado8=sSolapamiento8['CantidadPalabras'].tolist()




def graphWords(x1:list,y1:list,x2:list,y2:list,x3:list,y3:list,x4:list,y4:list,x5:list,y5:list,x6:list,y6:list,x7:list,y7:list,x8:list,y8:list):
    plt.figure(figsize=(12, 8))
    plt.xlabel('Words',fontsize=15);
    plt.ylabel('Time(s)',fontsize=15);
    plt.plot(x1, y1, 's', color='red',label=f"1",markersize=10)
    plt.plot(x2, y2, 's', color='blue',label=f"2",markersize=10)
    plt.plot(x3, y3, 's', color='green',label=f"3",markersize=10)
    plt.plot(x4, y4, 's', color='gray',label=f"4",markersize=10)
    plt.plot(x5, y5, 's', color='black',label=f"5",markersize=10)
    plt.plot(x6, y6, 's', color='orange',label=f"6",markersize=10)
    plt.plot(x7, y7, 's', color='purple',label=f"7",markersize=10)
    plt.plot(x8, y8, 's', color='brown',label=f"8",markersize=10)
    plt.legend(fontsize=15,loc='lower right')
    plt.tick_params(axis="both", labelsize=15)
    plt.show()

graphWords(palabrasSinSolapado1,tiempoSinSolapado1,palabrasSinSolapado2,tiempoSinSolapado2,palabrasSinSolapado3,tiempoSinSolapado3,palabrasSinSolapado4,tiempoSinSolapado4,palabrasSinSolapado5,tiempoSinSolapado5,palabrasSinSolapado6,tiempoSinSolapado6,palabrasSinSolapado7,tiempoSinSolapado7,palabrasSinSolapado8,tiempoSinSolapado8)
print(sum(finalTime['Tiempo'])/60)