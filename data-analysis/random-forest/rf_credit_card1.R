library(tidyverse)
library(e1071)
library(rpart)
library(randomForest)

# 加载信用卡还款数据，分析违约率-----------------------------------------------------------

card <- read.csv("https://raw.githubusercontent.com/cystanford/credit_default/master/UCI_Credit_Card.csv", stringsAsFactors =FALSE) %>% 
  as_tibble()

summary(card)

card$default.payment.next.month <- as_factor(card$default.payment.next.month)

# 分割数据集---------------------------------------------------------------------------

set.seed(1009)
train_index <- sample.int(nrow(card), nrow(card) * 0.75)

card.train <- card[train_index, -1] #删除ID列 
card.test <- card[-train_index, -1]

names(card.train)

# 支持向量机--------------------------------------

# 标准化特征
card.train.svm <- card.train[, -24] %>% scale() %>% as_tibble() %>% 
  mutate(default.payment.next.month = card.train$default.payment.next.month)

card.test.svm <- card.test[, -24] %>% scale() %>% as_tibble() %>% 
  mutate(default.payment.next.month = card.test$default.payment.next.month)

# card.train.svm.model <- tune.svm(default.payment.next.month ~ ., data = card.train.svm, 
#                                  gamma = 10^(-3:-1), cost = c(0.001, 0.01, 0.1, 1, 5 ,10 , 20))

card.train.svm.model <- svm(default.payment.next.month ~ ., data = card.train.svm, kernel = "radial", gamma = 0.1, cost = 5)

summary(card.train.svm.model)

# 预测
cancer.test.svm.model <- predict(card.train.svm.model, newdata = card.test.svm)

svm_tp <- table(pred = cancer.test.svm.model, true = card.test.svm$default.payment.next.month)

(svm_ac <- sum(diag(svm_tp) / sum(svm_tp))) # 0.8232

# 决策树------------------------------------------

card.train.dtree.model <- rpart(default.payment.next.month ~ ., data = card.train)

# 检查每次分裂的误差
print(card.train.dtree.model$cptable)

plotcp(card.train.dtree.model) # 选择 size 2

# 剪枝
prune.card.train.dtree.model <- prune(tree = card.train.dtree.model, cp = 0.01)

plotcp(prune.card.train.dtree.model)

# 预测
card.test.dtree.model <- predict(prune.card.train.dtree.model, newdata = card.test)

card.test.dtree.model <- as_tibble(card.test.dtree.model)

for (i in 1:nrow(card.test.dtree.model)) {
  card.test.dtree.model$result[i] <- names(which.max(as_tibble(card.test.dtree.model)[i,])) %>% as.numeric() 
}

dtree_tp <- table(pred = card.test.dtree.model$result, true = card.test$default.payment.next.month)

(dtree_ac <- sum(diag(dtree_tp) / sum(dtree_tp))) # 0.8268

#　随机森林------------------------------------------

card.train.rf.model <- randomForest(default.payment.next.month ~ .,data = card.train, mtry=2, ntree = 1000)

plot(card.train.rf.model)

card.train.rf.model <- randomForest(default.payment.next.month ~ .,data = card.train, mtry=2, ntree = 200)

card.test.rf.model <- predict(card.train.rf.model, newdata = card.test)

rf_tp <- table(pred = card.test.rf.model, true = card.test$default.payment.next.month)

(dtree_ac <- sum(diag(rf_tp) / sum(rf_tp))) # 0.8245

