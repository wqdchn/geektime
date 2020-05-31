# @program: PyDemo
# @description: 数据分析实战45讲练习：用EM算法对王者荣耀英雄进行划分
# @author: wqdong
# @create: 2020-05-31 14:44

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

# n_components：即高斯混合模型的个数
# covariance_type：代表协方差类型
# max_iter：代表最大迭代次数
# gmm = GaussianMixture(n_components=1, covariance_type='full', max_iter=100)

data_url = 'https://raw.githubusercontent.com/cystanford/EM_data/master/heros.csv'
data = pd.read_csv(data_url, encoding='gb18030')

print(data.head(10))
print(data.columns.values)

features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力',
            u'法力成长', u'初始法力', u'最高物攻', u'物攻成长',
            u'初始物攻', u'最大物防', u'物防成长', u'初始物防',
            u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血',
            u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝',
            u'最大攻速', u'攻击范围']

data = data[features]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 用热力图呈现features_mean字段之间的相关性
corr = data[features].corr()
plt.figure(figsize=(14, 14))
sns.heatmap(corr, annot=True)
# plt.show()

# 相关性大的属性保留一个，因此可以对属性进行降维
features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻',
                   u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血',
                   u'最大每5秒回蓝', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data[features_remain]
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})

# 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
ss = StandardScaler()
data_fit = ss.fit_transform(data)

# 构造GMM聚类
gmm = GaussianMixture(n_components=10, covariance_type='full')
gmm.fit(data_fit)  # 训练数据
prediction = gmm.predict(data_fit)
print(prediction)

# 将分组结果输出
data.insert(0, '分组', prediction)

print(data)