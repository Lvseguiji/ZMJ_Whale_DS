import pandas as pd
import numpy as np

titanic_df = pd.read_csv('csv/titanic_train.csv')
# print(titanic_df.head())

# 预处理
age = titanic_df['Age']
print('age中有', len(titanic_df['Age'][titanic_df.Age.isnull()]), '个none值\n')  # how many none values in 'Age' columns

# good_ages = titanic_df['Age'][titanic_df.Age.isnull() == False]
# avg_good_ages = sum(good_ages)/len(good_ages)
# print(avg_good_ages)

mean_good_ages = titanic_df['Age'].mean()  # mean可以自动过滤缺失值，计算
print('age mean: ', mean_good_ages, '\n')

## 计算每个船舱平均费用
p_class = sorted(titanic_df['Pclass'].unique().tolist())  # 获取所有船舱等级
print('船舱等级：', p_class, '\n')
fare_by_class = {}
for c in p_class:
    mean_fare = titanic_df['Fare'][titanic_df.Pclass == c].mean()
    fare_by_class[c] = round(mean_fare, 3)
print('每个等级的船舱平均费用：', fare_by_class, '\n')

## 生成pivot table 透视表
passenger_survival = titanic_df.pivot_table(index='Pclass', values='Survived', aggfunc=np.mean)
print(passenger_survival)

passenger_age = titanic_df.pivot_table(index='Pclass', values='Age')  # 默认求均值
print(passenger_age)

port_stats = titanic_df.pivot_table(index='Embarked', values=['Fare', 'Survived'], aggfunc=np.sum)
print(port_stats, '\n')

## 删除存在缺失值的列或行
drop_na_columns = titanic_df.dropna(axis=1)  # 删列
new_titanic_survival = titanic_df.dropna(axis=0, subset=['Age', 'Sex'])  # subset查看哪些列

## 排序，重置索引
## reset_index(drop=True), 删除当前的索引，再重置
## drop=False, 将当前索引返回列表中，再重置, 默认值
ordered_titanic_survival = titanic_df.sort_values("Age", ascending=False).reset_index(drop=True)
print(ordered_titanic_survival.head())

## set_index(drop=True)，将某一列作为index，并在原表中删除，默认值
## drop=False，将某一列作为index，并在原表中保留
set_id_index = titanic_df.set_index('PassengerId', drop=False)
print(set_id_index.head())


## 使用apply， 默认axis=0，按照列计算
def to_cns(row):
    if row.Survived == 1:
        return '生'
    else:
        return '死'


survive_to_cns = titanic_df['Survived'].apply(lambda x: ('生' if x == 1 else '死'))
survive_to_cns2 = titanic_df.apply(to_cns, axis=1)  # 逐行查询
print(survive_to_cns.head())
print(survive_to_cns2.head())

##计算每列有多少null值
def not_null_count(column):
    col_null = column[column.isnull()]
    return len(col_null)


column_null_count = titanic_df.apply(not_null_count)
print(column_null_count)

