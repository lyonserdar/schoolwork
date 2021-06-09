# Clustering

## K-Means

### R Code:

```
DataFrame <- read.csv("./filename.csv")
attach(DataFrame)
set.seed(7)
Groups <- kmeans(DataFrame[1:5], 3)
Clusters <- data.frame(Groups$cluster, DataFrame)
Centers <- data.frame(Groups$size, Groups$centers)
```

Use only numeric values to calculate the kmeans. (e.g., `DataFrame[1:5]`)

`Clusters <- data.frame(Groups$cluster, DataFrame$labelField)`

### RapidMiner

Operators:

1. Read CSV
2. Clustering

You can use `Multiply` operator to duplicate the input data.
