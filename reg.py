import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression




#Load dataset
df = pd.read_excel('datasetCiclosTiempos.xlsx')
dataset=df[['Nivel','Genero','Solapamiento','Secciones','CantidadPalabras','ScoreA']]


X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values


# Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

#categorical for genre text
labelencoder_X = LabelEncoder()
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])

ct = make_column_transformer(( OneHotEncoder(), [1]), remainder='passthrough')
X = np.array(ct.fit_transform(X))

#Cleaning firsts column from dataset to have 1-5 columns, 2 dummies and 3 original values
X=X[:,1:]

#categorical for overlapping text
X[:,3] = labelencoder_X.fit_transform(X[:, 3])
ct=make_column_transformer((OneHotEncoder(),[3]),remainder='passthrough')
X=np.array(ct.fit_transform(X))


# Dividir el data set en conjunto de entrenamiento y en conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 0)

#adjusting the model with the train data


regression=LinearRegression()
regression.fit(X_train,y_train)

#making predictions 
yPred= regression.predict(X_test)

import statsmodels.api as sm
##Automatized
def backwardElimination(x, sl):    
    numVars = len(x[0])    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        if maxVar > sl:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    x = np.delete(x, j, 1)    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5,6]]
X_Modeled = backwardElimination(X_opt, SL)
