library(rpart)
library(tidyverse)
library(partykit)
library(rpart.plot)

# 泰坦尼克数据------------------------------------------------------

titanic.train <- read.csv("https://raw.githubusercontent.com/wqdchn/geektime/master/data-analysis/titanic-survival-pred/data/train.csv",
                          stringsAsFactors =FALSE) %>% as_tibble()

titanic.test <- read.csv("https://raw.githubusercontent.com/wqdchn/geektime/master/data-analysis/titanic-survival-pred/data/test.csv", 
                         stringsAsFactors =FALSE) %>% as_tibble()

titanic.train
titanic.test

summary(titanic.train)
summary(titanic.test)

# 预处理-----------------------------------------------------------

# 年龄Age的NA值用均值填充
age_index <- which(is.na(titanic.train$Age)) 

titanic.train$Age[age_index] <- mean(titanic.train$Age, na.rm = T)

age_index <- which(is.na(titanic.test$Age)) 

titanic.test$Age[age_index]<- mean(titanic.test$Age, na.rm = T)

# 票价Fare的NA值用均值填充

fare_index <- which(is.na(titanic.test$Fare))

titanic.test$Fare[fare_index] <- mean(titanic.test$Fare, na.rm = T)

# 船舱Cabin的缺失值多无法补充，注意不是NA是""

which(titanic.train$Cabin == "")
which(titanic.test$Cabin == "")

# 登陆港口Embarked有少量缺失值

titanic.train$Embarked %>% table()

`%notin%` <- Negate(`%in%`)
filter(titanic.train, Embarked %notin% c("S", "Q", "C"))
filter(titanic.test, Embarked %notin% c("S", "Q", "C"))

embarked_index <- which(titanic.train$Embarked == "")

titanic.train$Embarked[embarked_index] <- "S"

# 特征选择----------------------------------------------------------

titanic.train <- select(titanic.train, -Name, -Cabin)

titanic.test <- select(titanic.test, -Name, -Cabin)

titanic.train

titanic.test

for (i in 1:nrow(titanic.train)) {

  # 性别字符串转为数字
  if (titanic.train$Sex[i] == "male") {
    titanic.train$Sex[i] <- 0
  } else {
    titanic.train$Sex[i] <- 1
  }

  # 港口字符串转为数字
  if (titanic.train$Embarked[i] == "C") {
    titanic.train$Embarked[i] <- 0
  } else if (titanic.train$Embarked[i] == "S") {
    titanic.train$Embarked[i] <- 1
  } else {
    titanic.train$Embarked[i] <- 2
  }
  
}

titanic.train$Sex <- as.numeric(titanic.train$Sex)
titanic.train$Embarked <- as.numeric(titanic.train$Embarked)

for (i in 1:nrow(titanic.test)) {
  
  # 性别字符串转为数字
  if (titanic.test$Sex[i] == "male") {
    titanic.test$Sex[i] <- 0
  } else {
    titanic.test$Sex[i] <- 1
  }
  
  # 港口字符串转为数字
  if (titanic.test$Embarked[i] == "C") {
    titanic.test$Embarked[i] <- 0
  } else if (titanic.test$Embarked[i] == "S") {
    titanic.test$Embarked[i] <- 1
  } else {
    titanic.test$Embarked[i] <- 2
  }
  
}

titanic.test$Sex <- as.numeric(titanic.test$Sex)
titanic.test$Embarked <- as.numeric(titanic.test$Embarked)

titanic.train %>% summary()

titanic.test %>% summary()

# 构造决策树----------------------------------------------------------

tree.titanic.train <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch +  Fare + Embarked, data = titanic.train)

summary(tree.titanic.train)

rpart.plot(tree.titanic.train)

# 检查每次分裂的误差
print(tree.titanic.train$cptable)

plotcp(tree.titanic.train) # 选择 size 6

(cp <- min(tree.titanic.train$cptable[6, ]))

# 剪枝
prune.tree.titanic.train <- prune(tree = tree.titanic.train, cp = cp)

plotcp(tree.titanic.train)

rpart.plot(tree.titanic.train)

# 测试集----------------------------------------------------------------

party.titanic.test <- predict(prune.tree.titanic.train, newdata = titanic.test) %>% as_tibble()

# 残念，测试集没有生存结果.....
# titanic.test$Survived
# 什么鬼...

party.titanic.trian <- predict(prune.tree.titanic.train, newdata = titanic.train) %>% as_tibble() 

titanic.train$Survived

for (i in 1:nrow(party.titanic.trian)) {
  if(party.titanic.trian$value[i] > 0.5 ){
    party.titanic.trian$result[i] <- 1
  }else{
    party.titanic.trian$result[i] <- 0
  }
}

party.titanic.trian

ac <- 0

for (i in 1:nrow(party.titanic.trian)) {
  if (party.titanic.trian$result[i] == titanic.train$Survived[i]){
    ac = ac + 1
  }
}

(ac = ac / nrow(party.titanic.trian)) # 0.819

