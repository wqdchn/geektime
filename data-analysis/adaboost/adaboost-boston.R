library(tidyverse)
library(gbm)      # for original implementation of regular and stochastic GBMs
library(xgboost)  # for fitting extreme gradient boosting

library(rpart)

library(MLmetrics)

# 加载波士顿房价数据集--------------------------------------------------

boston <- MASS::Boston %>% as_tibble()

summary(boston)

# 分割数据集-----------------------------------------------------------

set.seed(1007)
train_index <- sample.int(nrow(boston), nrow(boston) * 0.75)

boston.train <- boston[train_index, ]
boston.test <- boston[-train_index, ]

# 决策树---------------------------------------------------------------

boston.train.dt1 <- rpart(
  formula = medv ~ .,
  data    = boston.train,
  method  = "anova"
)

rpart.plot::rpart.plot(boston.train.dt1)

plotcp(boston.train.dt1)

boston.test.dt1 <- predict(boston.train.dt1, newdata = boston.test)

MSE(boston.test.dt1, boston.test$medv)

# 25.15582

# Basci Gradient boosting machines-------------------------------------------------------------

set.seed(1008)

boston.train.gbm1 <- gbm(
  formula = medv ~ .,
  data = boston.train,
  distribution = "gaussian",  # SSE loss function
  n.trees = 5000,
  shrinkage = 0.1,
  interaction.depth = 3,
  n.minobsinnode = 10,
  cv.folds = 10
)

best <- which.min(boston.train.gbm1$cv.error)

sqrt(boston.train.gbm1$cv.error[best])

gbm.perf(boston.train.gbm1, method = "cv")

boston.test.gbm1 <- predict(boston.train.gbm1, newdata = boston.test)

MSE(boston.test.gbm1, boston.test$medv)

# 9.675317

# extreme GBMs-----------------------------------------------------

boston.train.xgbm1 <- xgb.cv(
  data = boston.train[,-14] %>% as.matrix(),
  label = boston.train$medv,
  nrounds = 1000,
  objective = "reg:linear",
  early_stopping_rounds = 50, 
  nfold = 10,
  params = list(
    eta = 0.1,
    max_depth = 3,
    min_child_weight = 3,
    subsample = 0.8,
    colsample_bytree = 1.0),
  verbose = 2
)

min(boston.train.xgbm1$evaluation_log$test_rmse_mean)

# 3.204295

# 训练--------------------------------------------------------

hyper_grid <- expand.grid(
  eta = 0.01,
  max_depth = 3, 
  min_child_weight = 3,
  subsample = 0.5, 
  colsample_bytree = 0.5,
  gamma = c(0, 1, 10, 100, 1000),
  lambda = c(0, 1e-2, 0.1, 1, 100, 1000, 10000),
  alpha = c(0, 1e-2, 0.1, 1, 100, 1000, 10000),
  rmse = 0,          # a place to dump RMSE results
  trees = 0          # a place to dump required number of trees
)

for(i in seq_len(nrow(hyper_grid))) {
  set.seed(1009)
  m <- xgb.cv(
    data = boston.train[,-14] %>% as.matrix(),
    label = boston.train$medv,
    nrounds = 1000,
    objective = "reg:linear",
    early_stopping_rounds = 50, 
    nfold = 10,
    verbose = 0,
    params = list( 
      eta = hyper_grid$eta[i], 
      max_depth = hyper_grid$max_depth[i],
      min_child_weight = hyper_grid$min_child_weight[i],
      subsample = hyper_grid$subsample[i],
      colsample_bytree = hyper_grid$colsample_bytree[i],
      gamma = hyper_grid$gamma[i], 
      lambda = hyper_grid$lambda[i], 
      alpha = hyper_grid$alpha[i]
    ) 
  )
  hyper_grid$rmse[i] <- min(m$evaluation_log$test_rmse_mean)
  hyper_grid$trees[i] <- m$best_iteration
}

# results
hyper_grid %>%
  filter(rmse > 0) %>%
  arrange(rmse) %>%
  glimpse()

params <- list(
  eta = 0.01,
  max_depth = 3,
  min_child_weight = 3,
  subsample = 0.5,
  colsample_bytree = 0.5
)

# 拟合----------------------------------------------------------

boston.train.xgbm1.fit <- xgboost(
  # params = params,
  params = list(
    eta = 0.1,
    max_depth = 3,
    min_child_weight = 3,
    subsample = 0.8,
    colsample_bytree = 1.0),
  data = boston.train[,-14] %>% as.matrix(),
  label = boston.train$medv,
  nrounds = 500,
  objective = "reg:linear",
  verbose = 2
)

# 预测---------------------------------------------------------

boston.test.xgbm1 <- predict(boston.train.xgbm1.fit, newdata = boston.test[,-14] %>% as.matrix())

MSE(boston.test.xgbm1, boston.test$medv)

# 9.475446

