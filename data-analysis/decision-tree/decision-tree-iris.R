library(rpart)
library(tidyverse)
library(partykit)
library(rpart.plot)

# irir示例数据------------------------------------------
head(iris)

dim(iris)

summary(iris)

# 分割训练集与测试集
set.seed(1001)
train_index <- sample.int(150, 100)

iris.train <- iris[train_index, ]
iris.test <- iris[-train_index, ]

dim(iris.train)
dim(iris.test)

# 训练模型
tree.iris <- rpart(Species ~ ., data = iris.train)

summary(tree.iris)

rpart.plot(tree.iris)

# 检查每次分裂的误差
print(tree.iris$cptable)

plotcp(tree.iris) # 选择 size 3

(cp <- min(tree.iris$cptable[3, ]))

# 剪枝
prune.tree.iris <- prune(tree = tree.iris, cp = cp)

plotcp(prune.tree.iris)

rpart.plot(prune.tree.iris)

# 比较 
plot(as.party(tree.iris))
plot(as.party(prune.tree.iris))

# 测试集
party.isis.test <- predict(prune.tree.iris, newdata = iris.test)

party.isis.test <- as_tibble(party.isis.test) 

for (i in 1:nrow(party.isis.test)) {
  party.isis.test$result[i] <- names(which.max(as_tibble(party.isis.test)[i,]))
}


# 检查结果
party.isis.test$result
                                      
as.character(iris.test$Species)

ac <- 0

for (i in 1:nrow(party.isis.test)) {
  if (party.isis.test$result[i] == as.character(iris.test$Species)[i]){
    ac = ac + 1
  }
}

(ac = ac / 50)

