
## Introdução
Olá, pessoal! Hoje vamos falar sobre um assunto muito interessante: aprendizado de máquina utilizando uma ferramenta muito especial que faz até parecer magia. Venha conhecer o mundo 
do R.

## O que é R
R é como uma caixa de ferramentas mágica para trabalhar com números e dados. Foi criado há muitos anos, em 1993, por dois caras chamados Ross e Robert. Eles queriam uma maneira poderosa e flexível de fazer estatísticas e gráficos. Hoje, usamos R para analisar dados, criar gráficos e até mesmo para fazer previsões sobre o futuro!

## O que é Machine Learning
Machine Learning é uma tecnologia que faz os computadores aprenderem com os dados, assim como nós aprendemos com nossas experiências. Foi desenvolvido na década de 1950 por cientistas que queriam que as máquinas pudessem melhorar suas habilidades sozinhas. Ele resolve problemas como reconhecer rostos em fotos, prever o tempo e até recomendar filmes para você assistir!

## Mão na Massa, Quero Dizer, no Código

### Aprendizado Não Supervisionado

O aprendizado não supervisionado é quando o computador tenta entender os dados sem uma resposta certa para comparar. É como se você tivesse um monte de peças de LEGO e tentasse descobrir como montar algo, sem saber o que deveria construir. Em R, usamos pacotes como `cluster` e `factoextra` para isso. Veja um exemplo de código:

```r
library(cluster)
dados <- iris[, -5]
modelo <- kmeans(dados, centers = 3)
plot(dados, col = modelo$cluster)
```
<!-- precisa incluir a figura e explicar melhor o resultado -->

### Aprendizado Supervisionado

O aprendizado supervisionado é quando o computador aprende com exemplos que já têm respostas certas. É como ensinar seu cachorro a sentar, dando um petisco toda vez que ele faz o truque certo. Em R, usamos pacotes como `caret` e `randomForest`. Vamos treinar um modelo de árvore de decisão para classificar as espécies de flores com base em suas características e, em seguida, plotar um gráfico comparando as previsões com os dados reais.

```r
# Carregar pacotes necessários
library(caret)
library(randomForest)
library(ggplot2)

# Carregar o conjunto de dados iris
dados <- iris

# Dividir os dados em conjunto de treino e teste
set.seed(123) # Para reprodutibilidade
indices <- createDataPartition(dados$Species, p = 0.7, list = FALSE)
dados_treino <- dados[indices, ]
dados_teste <- dados[-indices, ]

# Treinar o modelo com randomForest
modelo_rf <- train(Species ~ ., data = dados_treino, method = "rf")

# Fazer previsões com o modelo
previsoes <- predict(modelo_rf, dados_teste)

# Criar um dataframe para plotar
resultado <- data.frame(Real = dados_teste$Species, Previsto = previsoes)

# Plotar os resultados
ggplot(resultado, aes(x = Real, fill = Previsto)) +
  geom_bar(position = "dodge") +
  labs(title = "Comparação entre Classificações Reais e Previstas",
       x = "Espécies Reais",
       y = "Número de Ocorrências") +
  theme_minimal()

# Mostrar o modelo e as previsões
print(modelo_rf)
print(head(resultado))
```

## Vamos Juntos!

Se você gostou e quer saber mais sobre tecnologia e programação, siga minhas redes sociais para mais dicas e tutoriais incríveis! Curta e compartilhe para ajudar outras pessoas a aprender também. 


Ilustrações de capa: gerada pele lexica.art
Conteúdo gerado por: ChatGPT e revisões humanas




https://web.dio.me/articles/analise-de-dados-com-r-e-machine-learning-uma-introducao?back=%2Farticles&open-modal=true&page=1&order=oldest

prj/www/tec-write