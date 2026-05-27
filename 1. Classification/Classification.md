#### Aula 22/10/25

## Label encoding
Transforma valores categóricos (ex: nomes) em números inteiros.
**Onde usar:** Quando a ordem dos valores faz sentido (ex: “Baixo”, “Médio”, “Alto”).
Algoritmos que conseguem lidar bem com rótulos codificados (ex: árvores de decisão).

Cuidado:
Pode introduzir uma ordem que não existe. Ex: 
Se “Verde” = 0, “Azul” = 1, “Vermelho” = 2
 → o modelo pode achar que Vermelho > Azul > Verde, o que pode ser errado.

Código exemplo

```
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
cores = ['vermelho', 'azul', 'verde']
le.fit_transform(cores)

// Saída: array([2, 0, 1])
```

### One-hot encoding
Converte cada categoria em uma coluna binária (0 ou 1).
Ou seja, representa cada valor sem nenhuma ordem implícita.
**Onde usar:** Quando as categorias são nominais (sem ordem).
Usado com modelos lineares, redes neurais, etc.
 
**Desvantagem:** Cria muitas colunas se houver muitas categorias → pode aumentar muito a dimensionalidade.

## Naive Bayes
Classificador probabilístico baseado no Teorema de Bayes, que assume que as variáveis são independentes entre si (daí o "naive").

**Onde usar:**
Classificação de texto (spam, análise de sentimentos)
Diagnóstico médico Problemas com muitos dados e/ou poucas amostras.
** Como funciona:**
 Calcula a probabilidade de cada classe com base nas características de entrada e escolhe a mais provável.

**Tipos principais:**
- Gaussian Naive Bayes: para dados contínuos (assume distribuição normal)
- Multinomial Naive Bayes: para contagens (ideal para texto)
- Bernoulli Naive Bayes: para dados binários (0/1)

**Classificação:**
- True Positive - Dados que eram de uma classe e foram preditas corretamente
- False Positive - Dados que não eram de uma classe e foram preditas corretamente 
- True Negative - Dados que eram de uma classe e foram preditas incorretamente 
- False Negative - Dados que não eram de uma classe e foram preditas incorretamente 

**Acurácia:** Proporção de previsões corretas (tanto verdadeiros positivos quanto verdadeiros negativos) sobre o total de previsões. 

**Precisão:** Proporção de exemplos positivos corretamente previstos entre todos os que o modelo previu como positivos. 

**Recall:** Proporção de exemplos positivos corretamente previstos entre todos os que realmente são positivos. 

**F1_Score:** Média harmônica entre Precisão e Recall. Equilibra os dois quando há desequilíbrio entre classes. 

**Matriz de confusão:** Tabela que mostra a comparação entre as previsões do modelo e os valores reais. 

```
//Código exemplo
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

dados = pd.DataFrame({'cor': ['vermelho', 'azul', 'verde']})

ohe = OneHotEncoder(sparse=False)
ohe.fit_transform(dados[['cor']])
# Saída:
# array([[0., 0., 1.],
#        [1., 0., 0.],
#        [0., 1., 0.]])
```

## KNN (k-Nearest Neighbors)
Algoritmo que classifica um ponto novo pela classe dos seus k vizinhos mais próximos no espaço.
**Onde usar:**
 Classificação simples, reconhecimento de padrões, quando não se sabe a distribuição dos dados.
**Como funciona:**
Calcula distâncias, pega os k vizinhos mais próximos e usa a classe mais comum deles.
**Ponto importante:**
 Escolher bem o k e normalizar os dados.
