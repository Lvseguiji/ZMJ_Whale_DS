import pandas as pd
import os

print('当前路径：', os.getcwd()) #打印出当前工作路径

data = pd.read_csv("./csv/food_info.csv")
print(data.dtypes)
# print(data.head())
# print(data.columns)
print('\nshape: ', data.shape, '\n')

# print(data.loc[0])  # 1st row

# print(data.loc[3:5])  # 包括头和尾(index 3,4,5)

# print(data.loc[[2,3,5]]) # 选取对应的index行

# print(data['Water_(g)'])

# print(data[['Water_(g)','Ash_(g)']])

print(data.loc[[3,4,6],'Water_(g)'])

# loc 包头包尾， iloc 包头去尾
print(data.loc[3:5,['NDB_No','Shrt_Desc']])
print(data.iloc[3:6,0:2])

print("\n1. get all columns endswith (g):")
col_names = data.columns.tolist()
g_columns = []
for i in col_names:
    if i.endswith("(g)"):
        g_columns.append(i)
g_data = data[g_columns]
print(g_data.head())

# 添加新的一列
print("\n2. 添加新的一列:")
iron_gram = data['Iron_(mg)']/1000
data['Iron_(g)'] = iron_gram
print(data[["Iron_(mg)","Iron_(g)"]])
print(data.shape)

# preprocess
print("\n3.预处理:\n原始数据")
print(data['Sodium_(mg)'])
data.sort_values("Sodium_(mg)", inplace=True, ascending=False)  # 不创建新对象，直接对原始对象修改
print('新数据\n',data['Sodium_(mg)'])
