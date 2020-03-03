# Algoritmo para prever sobreviventes no titanic

Primeiro carregaremos o dataset de treino ```train.csv``` 
```{r}
titanic.train <- read.csv(file="train.csv",stringsAsFactors = FALSE,  header=TRUE)

```
Agora carregaremos o dataset de test ```test.csv``` :

```{r}
titanic.test <- read.csv(file="test.csv",stringsAsFactors = FALSE,  header=TRUE)

```
Na primeira linha abaixo checamos a media das idades e como o valor retornado é ```NA```, na linha seguinte setamos


```na.rm=TRUE``` para não considerar os valores não disponveis na contagem e fazemos o mesmo para o dataframe de test:

```{r}
median(titanic.train$Age)
median(titanic.train$Age, na.rm=TRUE)
median(titanic.test$Age, na.rm=TRUE)

```
Para tratar e limpar os dataframes pra evitar de reescrever o códígo duas vezes , vamos criar uma coluna no ```titanic.train``` chama ```IsTrainSet``` e setaremos todos os valores para ```TRUE``` . Já em  ```titanic.test``` faremos o mesmo e setaremos a coluna com o valor false

```{r}
titanic.train$IsTrainSet <- TRUE
tail(titanic.train$IsTrainSet)

titanic.test$IsTrainSet <- FALSE


ncol(titanic.train)
ncol(titanic.test)

```


```{r}
names(titanic.train)
names(titanic.test)

titanic.test$Survived <- NA
ncol(titanic.test)
```
Agora faaremos um merge de ```titanic.train``` e ```titanic.test``` em ```titanic.full``` assim manipularemos apenas um dataframe na limpeza.

```{r}
titanic.full <- rbind(titanic.train, titanic.test)


```


```{r}
table(titanic.full$IsTrainSet)
```


```{r}
table(titanic.full$Embarked)

```


```{r}
titanic.full$Embarked == ""

```
Vamos substituir na coluna ```Embarked``` os valores vazios por "S" , que é o valor com maior numero de ocorrencias.

```{r}

titanic.full[titanic.full$Embarked=="","Embarked"] <- "S"
table(titanic.full$Embarked)

```

Definimos duas variaveis com valor da media da idade e do fare respectivamente
```{r}

age.median <- median(titanic.full$Age, na.rm=TRUE)
fare.median <- median(titanic.full$Fare, na.rm=TRUE)

```
Agora inserimos a media do Age nos valores vazios da coluna

```{r}
titanic.full[is.na(titanic.full$Age),"Age"] <- age.median


```

```{r}
fare.median <- median(titanic.full$Fare, na.rm = TRUE)
titanic.full[is.na(titanic.full$Fare),"Fare"] <- fare.median
```

Algoritimos de IA não trabalham muito bem com etiquetas. Então vamos transformar em fatos 
```{r}
titanic.full$Pclass <- as.factor(titanic.full$Pclass)
titanic.full$Sex <- as.factor(titanic.full$Sex)
titanic.full$Embarked <- as.factor(titanic.full$Embarked)
```

agora vamos splitar o dataset full
```{r}
titanic.train <- titanic.full[titanic.full$IsTrainSet == TRUE,]
titanic.test <- titanic.full[titanic.full$IsTrainSet == FALSE,]

```

```{r}
titanic.train$Survived <- as.factor(titanic.train$Survived)

```

```{r}
survived.equation <- "Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked"

survived.formula <- as.formula(survived.equation)

install.packages("randomForest")
library(randomForest)

titanic.model <- randomForest(formula= survived.formula, data= titanic.train, ntree= 500, mtry = 3, nodesize = 0.01 * nrow(titanic.test))


```



```{r}

titanic.model <- randomForest(formula= survived.formula, data= titanic.train, ntree= 500, mtry = 3, nodesize = 0.01 * nrow(titanic.test))

```



```{r}

features.equation <- "Pclass + Sex + Age + SibSp + Parch + Fare + Embarked"

Survived<-predict(titanic.model, newdata = titanic.test)

```



```{r}


PassengerId <- titanic.test$PassengerId
output.df <- as.data.frame(PassengerId)
output.df$Survived <- Survived

write.csv(output.df, file="Kaggle_submission.csv",row.names = FALSE)
```
