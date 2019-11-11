library(e1071)
library(tidyverse)
library(corrplot)

# 读取乳腺癌数据集--------------------------------------------------------

cancer <- read.csv("https://raw.githubusercontent.com/wqdchn/geektime/master/data-analysis/breast-cancer-svm/data/breast-cancer-data/data.csv",
                          stringsAsFactors =FALSE) %>% as_tibble()

names(cancer)

# 检查数据----------------------------------------------------------------

summary(cancer)

cancer <- select(cancer, -id)

# 将diagnosis字段替换为0或1，M表示恶性1，B表示良性记为0

unique(cancer$diagnosis)

cancer$diagnosis <- case_when(
  cancer$diagnosis == "M" ~ 1,
  cancer$diagnosis == "B" ~ 0
)

cancer_mean <- select(cancer, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean,
                      smoothness_mean, compactness_mean, concavity_mean, concave.points_mean,
                      symmetry_mean, fractal_dimension_mean)

ggplot(cancer) + geom_bar(aes(diagnosis))

corrplot(cor(cancer_mean[,-1], method = "pearson"), method = "number")

corrplot.mixed(cor(cancer_mean[,-1], method = "pearson"))

# 特征选择 & 分割数据集---------------------------------------------------------------

# features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'] 

set.seed(1002)
train_index <- sample.int(nrow(cancer_mean), nrow(cancer_mean) * 0.7)

cancer.trian <- cancer_mean[train_index, c('diagnosis','radius_mean','texture_mean', 'smoothness_mean',
                                           'compactness_mean','symmetry_mean', 'fractal_dimension_mean')]

cancer.test <- cancer_mean[-train_index, c('diagnosis','radius_mean','texture_mean', 'smoothness_mean',
                                           'compactness_mean','symmetry_mean', 'fractal_dimension_mean')]

# 标准化特征---------------------------------------------------------------

summary(cancer.trian)
summary(cancer.test)

cancer.trian[, -1] <- scale(cancer.trian[, -1])
cancer.test[, -1] <- scale(cancer.test[, -1])

summary(cancer.trian)
summary(cancer.test)

# 训练--------------------------------------------------------------------

cancer.svm <- tune.svm(diagnosis ~ ., data = cancer.trian, gamma = 10^(-10:-1), cost = c(0.001, 0.01, 0.1, 1, 5 ,10 , 20))

summary(cancer.svm)

cancer.svm <- svm(diagnosis ~ ., data = cancer.trian, kernel = "radial", gamma = 0.1, cost = 5)

# 测试--------------------------------------------------------------------

cancer.test.svm <- predict(cancer.svm, newdata = cancer.test)

cancer.test.svm <- case_when( # ???????????
  cancer.test.svm > 0.5 ~ 1,
  cancer.test.svm <= 0.5 ~ 0
)

(tp <- table(pred = cancer.test.svm , true = cancer.test$diagnosis))

(ac <- sum(diag(tp) / sum(tp)))

