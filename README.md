# Previsão Climática com Regressão Linear

Este projeto tem como objetivo realizar a previsão de temperatura para a cidade de Recife, utilizando dados climáticos obtidos por meio de uma API, que são armazenados no MongoDB. A partir desses dados, é aplicado um modelo de regressão linear para prever a temperatura com base em outras variáveis climáticas, como pressão e umidade.

## Como Funciona

1. **Obtenção dos Dados Climáticos:**  
   A API coleta dados climáticos em tempo real para a cidade de Recife (ou uma cidade configurada). Esses dados incluem informações como temperatura, umidade, pressão, entre outros.

2. **Armazenamento no MongoDB:**  
   Os dados coletados são armazenados em um banco de dados MongoDB, na coleção `orders`. Cada entrada no banco contém as informações climáticas do momento da coleta.

3. **Pré-processamento dos Dados:**  
   Após a coleta e armazenamento, os dados são extraídos do MongoDB e normalizados, preparando-os para o modelo de previsão.

4. **Modelo de Previsão:**  
   Utilizando regressão linear, o modelo é treinado com variáveis como pressão atmosférica e umidade para prever a temperatura em tempo futuro. O modelo é avaliado usando métricas como o erro quadrático médio (MSE) e o coeficiente de determinação (R²).

5. **Visualização:**  
   Após a previsão, é gerado um gráfico comparando os valores reais de temperatura com as previsões feitas pelo modelo, permitindo uma análise visual da precisão do modelo.

## Requisitos

- Python 3.x
- MongoDB
- Bibliotecas Python: `pandas`, `matplotlib`, `scikit-learn`, `pymongo`

## Métricas de Avaliação

### MSE (Erro Quadrático Médio):
O MSE é uma métrica que mede a diferença média entre os valores reais e os previstos, penalizando mais os erros maiores. Quanto menor o valor do MSE, melhor o modelo.

### R² (Coeficiente de Determinação):
O R² indica a proporção da variabilidade dos dados que é explicada pelo modelo. Um valor de R² perto de 1 significa que o modelo explica muito bem os dados. Se o R² for negativo ou muito baixo, significa que o modelo não está performando bem.


