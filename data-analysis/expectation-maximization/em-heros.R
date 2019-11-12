library(tidyverse)
library(mclust)
library(corrplot)

# 加载王者荣耀英雄数据------------------------------------------------

heros <- read.csv("https://raw.githubusercontent.com/cystanford/EM_data/master/heros.csv") %>% as_tibble()

summary(heros)

# 特征选择-----------------------------------------------------------

corrplot(cor(heros[,2:19], method = "pearson"), method = "number")

heros_remain <- select(heros, '英雄', '最大生命', '初始生命', '最大法力', '最高物攻', 
                              '初始物攻', '最大物防', '初始物防', '最大每5秒回血', 
                              '最大每5秒回蓝', '初始每5秒回蓝', '最大攻速', '攻击范围')

# 字段预处理----------------------------------------------------------------

heros_remain$攻击范围 <- case_when(
  heros_remain$攻击范围 == "远程" ~ 1,
  heros_remain$攻击范围 == "近战" ~ 0
)

str_view_all(heros_remain$最大攻速, "\\d+\\.\\d+")

heros_remain$最大攻速 <- str_extract_all(heros_remain$最大攻速, "\\d+\\.\\d+") %>% unlist() %>% as.double()

heros_remain

# 标准化---------------------------------------------------------------------

heros_remain[,-1] <- scale(heros_remain[,-1])


# 训练模型-------------------------------------------------------------------

em.heros.train <- Mclust(data = heros_remain, G=30)

summary(em.heros.train)

mutate(heros_remain[,1], em.heros.train$classification)

plot(em.heros.train)

