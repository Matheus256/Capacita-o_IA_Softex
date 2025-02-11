import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Criando um DataFrame de exemplo
dados = pd.DataFrame({
    'Tensão': [1.989, 1.725, 1.475],
    'pH': [4, 7, 10]
})
#pH 7 ----> Tensão 1.740

# Visualizando os dados
print(dados)

# Variável independente (X) e dependente (y)
X = dados[['Tensão']]
y = dados['pH']

# Dividindo em treino e teste
#X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.1, random_state=42)

# Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(X, y)

# Coeficiente e Intercepto
print(f"Coeficiente (β1): {modelo.coef_[0]}")
print(f"Intercepto (β0): {modelo.intercept_}")

# Fazendo previsões no conjunto de teste
y_pred = modelo.predict(X)

# Visualizando os dados e a linha de regressão
plt.scatter(X, y, color='blue', label='Dados')
plt.plot(X, y_pred, color='red', label='Linha de Regressão')
plt.xlabel('Tensão')
plt.ylabel('pH')
plt.title('Regressão Linear Simples')
plt.legend()
plt.show()
