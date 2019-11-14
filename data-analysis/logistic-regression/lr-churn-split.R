library(tidyverse)
library(rsample)
library(caret)
library(INLA)
library(vip)

# 加载员工数据集-----------------------------------------------

churn <- attrition %>% mutate_if(is.ordered, factor, ordered = FALSE)

summary(churn)

# ggplot(churn) + geom_bar(aes(Attrition)) + facet_grid(. ~ MonthlyIncome)
ggplot(churn) + geom_bar(aes(Attrition)) + facet_grid(. ~ OverTime)

# 分割数据集--------------------------------------------------

set.seed(1009)
churn_split <- initial_split(churn, prop = 0.7, strata = "Attrition")
churn_train <- training(churn_split)
churn_test  <- testing(churn_split)

# 简单模型----------------------------------------------------

model1 <- glm(Attrition ~ MonthlyIncome, family = "binomial", data = churn_train)
model2 <- glm(Attrition ~ OverTime, family = "binomial", data = churn_train)

tidy(model1)
tidy(model2)

exp(coef(model1))
exp(coef(model2))

# 多变量------------------------------------------------------

model3 <- glm(
  Attrition ~ MonthlyIncome + OverTime,
  family = "binomial", 
  data = churn_train
)

tidy(model3)


# 训练--------------------------------------------------------

set.seed(1010)
cv_model1 <- train(
  Attrition ~ MonthlyIncome + OverTime, 
  data = churn_train, 
  method = "glm",
  family = "binomial",
  trControl = trainControl(method = "cv", number = 10)
)

set.seed(1011)
cv_model2 <- train(
  Attrition ~ ., 
  data = churn_train, 
  method = "glm",
  family = "binomial",
  trControl = trainControl(method = "cv", number = 10)
)

summary(
  resamples(
    list(
      model1 = cv_model1, 
      model2 = cv_model2
    )
  )
)$statistics$Accuracy

# 预测-------------------------------------------------------

churn.test.pred <- predict(cv_model2, newdata = churn_test)

table(pred = churn.test.pred, true = churn_test$Attrition)

(ac <- (357 + 24) / 440)

# ROC-------------------------------------------------------

library(ROCR)

m1_prob <- predict(cv_model1, churn_train, type = "prob")$Yes
m2_prob <- predict(cv_model2, churn_train, type = "prob")$Yes


perf1 <- prediction(m1_prob, churn_train$Attrition) %>%
  performance(measure = "tpr", x.measure = "fpr")
perf2 <- prediction(m2_prob, churn_train$Attrition) %>%
  performance(measure = "tpr", x.measure = "fpr")


plot(perf1, col = "black", lty = 2)
plot(perf2, add = TRUE, col = "blue")
legend(0.8, 0.2, legend = c("cv_model1", "cv_model2"),
       col = c("black", "blue"), lty = 2:1, cex = 0.6)

