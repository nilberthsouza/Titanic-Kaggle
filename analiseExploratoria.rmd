```{r}
train <- read.csv(file="Documents/pythonprogram/Codigos-de-Data-Science/train.csv",header =TRUE)
head(train)
```

```{r}
freq <-table(train[,2])
freq
```

```{r}
#grafico de pizza 
pie(freq,main="sobreviventes",labels=c("61.6%","38.4%"),col=c(4,2))
legend("bottomleft",fill=c(4,2),legend=c("mortos","sobreviventes"))
```
```{r}


```
