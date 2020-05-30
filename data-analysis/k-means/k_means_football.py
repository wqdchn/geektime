# @program: PyDemo
# @description: 数据分析实战45讲练习：给20支亚洲球队做聚类
# @author: wqdong
# @create: 2020-05-30 14:04

from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

# 读取数据
data_url = 'https://raw.githubusercontent.com/cystanford/kmeans/master/data.csv'
data = pd.read_csv(data_url, encoding='gbk')

#print(data)

train_x = data[['2019年国际排名', '2018世界杯', '2015亚洲杯']]
df = pd.DataFrame(train_x)
km = KMeans(n_clusters=3)

# 规范化到[0,1]
min_max_scale = preprocessing.MinMaxScaler()
train_x = min_max_scale.fit_transform(train_x)

# kmeans算法
km.fit(train_x)
predict_y = km.predict(train_x)

# 合并聚类，查看结果
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类'}, axis=1, inplace=True)
print(result)