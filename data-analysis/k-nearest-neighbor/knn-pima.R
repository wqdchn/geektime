library(MASS)
library(tidyverse)
library(caret)
library(corrplot)

# 加载Pima糖尿病数据------------------------------------------------

pima <- bind_rows(Pima.tr,Pima.tr2,Pima.te)

summary(pima)

# bp字段的NA值用均值填充
pima$bp[which(is.na(pima$bp))] <-  mean(pima$bp, na.rm = T)

# skin字段的NA值用均值填充
pima$skin[which(is.na(pima$skin))] <- mean(pima$skin, na.rm = T)

# bmi字段的NA值用均值填充
pima$bmi[which(is.na(pima$bmi))] <- mean(pima$bmi, na.rm = T)

# 分割数据集--------------------------------------------------------
set.seed(1003)
train_index <- sample.int(nrow(pima), nrow(pima) * 0.7)

pima.train <- pima[train_index,]
pima.test <- pima[-train_index,]

table(pima.train$type)# 检查训练集结果的平衡性

names(pima.train)

corrplot(cor(pima.train[,-8], method = "pearson"), method = "number")

# 标准化------------------------------------------------------------

pima.train[,-8] <- scale(pima.train[,-8])
summary(pima.train)

pima.test[,-8] <- scale(pima.test[,-8])
summary(pima.test)

# 训练模型----------------------------------------------------------

grid <- expand.grid(k = seq(4, 20, by = 1))

control <- trainControl(method = "cv")

set.seed(1004)

knn.pima.train <- caret::train(type ~ ., data = pima.train, method = "knn", trControl = control, tuneGrid = grid)

# k = 5

# 测试---------------------------------------------------------------

knn.pima.test <- predict(knn.pima.train, newdata = pima.test)

table(knn.pima.test == pima.test$type)

(ac <- 192 / 250)

# 测试2--------------------------------------------------------------

knn.pima.test2 <- class::knn(pima.train[, -8], pima.test[, -8], pima.train[, 8], k = 5)

table(knn.pima.test2 == pima.test$type)

(ac <- 190 / 250)
