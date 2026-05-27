# SVM - Máquina de Vetores de Suporte

Forma de separar diferentes grupos de dados. 
- Vetores de suporte são os extremos de cada grupo. 
- O objetivo é conseguir a melhor margem possível.
- A margem é definida pela distância entre os extremos de cada grupo.
- A amplitude é a "Segurança" do algoritmo, quando maior, melhor.
  
### Convex Hull
- Ignora o que está no meio e identifica os extremos. 
- Irá traçar esses extremos e encontrar o menor vértice.

### Erros e Custo

O erro é quando uma intância do grupo A fica abaixo da linha que define o grupo B.

1/2 |w|² + c sigma i ai

**Parâmetro C** - Punição por classificação incorreta.  Um C alto tenta 100% de separação, o baixo permite mais erros.

**Kernel Trick** - As vezes os dados não podem ser separados por uma linha reta. O Kernel permite transformar os dados em outra dimensão, tornando possível separá-los. Existem 4 tipos:
1. Kernel Linear
2. Kernel Polinomial
3. Kernel Gaussiano (RBF/Radial)
4. Kernel Tangente Hiperbólica (Sigmoid)

## Considerações
### Vantagens
- Não é muito influenciado por ruídos.
- Utilizado para classificação e regressão.
- Aprende conceitos não presentes nos dados originais.
- Mais fácil de usar do que redes neurais.
### Desvantagens
- Lentidão.
- Black Box