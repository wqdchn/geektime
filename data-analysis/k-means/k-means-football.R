library(tidyverse)
library(NbClust)

# 加载数据------------------------------------------------------------------------

football <- read.csv("https://raw.githubusercontent.com/cystanford/kmeans/master/data.csv") %>% as_tibble()

summary(football)

# 特征标准化---------------------------------------------------------------------

football

football[,-1] <- apply(football[, -1], 2, function(x) { # [0-1]
  return((x - min(x)) / (max(x) - min(x)))
})

summary(football)

# 聚类---------------------------------------------------------------------------

football.kmeans <- NbClust(data = football[,-1], min.nc = 2, max.nc = 5, method = "kmeans")

set.seed(1005)
football.km <- kmeans(football[,-1], 3, nstart = 25)

mutate(football, clustering = football.km$cluster)

