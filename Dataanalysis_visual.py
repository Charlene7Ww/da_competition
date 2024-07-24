#!/usr/bin/env python
# coding: utf-8

# ## 1. 可视化

# #### 1.1 Tableau 可视化

# #### 发货地址分析
# * 发货地商品记录数、销售额、销量等的条形图或地图
# 
# #### 店铺分析
# * 销售额最好的10家店铺销售额条形图
# * 销售额最好的10家店铺价格等级与一级分类和二级分类堆积柱形图
# * 销售额最高的10家店铺的平均折扣力度比较

# #### 单品分析
# * 最热销（销量）的商品TOP10
# * 销售额最高的商品TOP10
# * 人气最高（收藏数）的商品TOP10
# * 库存最高的10款商品
# * 价格最高的TOP10商品
# 
# 

# #### 1.2. 使用wordArt制作词云
# * 商品名称词云
# * 商品发货地址词云

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


data = pd.read_csv('宠物商品详细信息_处理后.csv',engine ='python',encoding = 'utf-8')


# In[ ]:


data.info()


# In[ ]:


for i in data['商品名称']:
    print(i)


# ## 2. 挖掘建模

# In[ ]:


# 将评论数 名称修改为 总销量
data = data.rename(columns = {'评论数':'总销量'})


# In[ ]:


data.describe()


# In[ ]:


data.describe().columns


# In[ ]:


# 查看各变量之间的相关性,制作热力图


# In[ ]:


t = data[['商品现价', '商品原价', '商品库存', '宝贝收藏数', '描述评分',
       '服务评分', '物流评分', '销售额', '商品折扣', '平均评分', '总销量']]


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


plt.rcParams['font.sans-serif']=['SimHei'] #配置显示中文
plt.rcParams['axes.unicode_minus']=False #正常显示负号


# In[ ]:


plt.figure(figsize=(12,10))
sns.heatmap(np.abs(t.corr()),annot=True)
plt.show()


# ### 构建情感分析

# 文本情感分析:对宠物商品的整体评论文本进行情感分析，进一步的可以选择销售额TOP10的店铺或者类别的评论文本数据进行情感分析及观点提取，有选择性的对提取的观点制作词云图。
# * 单品销售额TOP10的商品情感得分和观点提取
# * 销售额TOP10店铺情感得分和观点提取
# * 所有评分水平都是“低于”的店铺的情感得分和观点提取
# * 还可以从其他角度进行文本分析，比如了解布偶猫、猫零食、魔法鱼等类别商品

# In[ ]:


df = data.groupby('店铺名称').sum().sort_values(by = ['销售额'],ascending =False)
df[:10]


# In[ ]:


shops = df[:10].index.tolist()
shops


# In[ ]:


cc=pd.read_csv("宠物商品评论数据.csv",encoding='utf-8',engine='python')


# In[ ]:


cc.info()


# In[ ]:


cc.head()


# #### 2.2 情感分析

# In[ ]:


import getpass


# In[ ]:


AppID = getpass.getpass('APPID')


# In[ ]:


ApiKey = getpass.getpass('APIKEY')
SecretKey = getpass.getpass('SecretKey')


# In[ ]:


from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = AppID
API_KEY = ApiKey
SECRET_KEY = SecretKey

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


# In[ ]:


# 封装成1个函数
def del_emoji(ss):
    text = ''
    for i in ss:
    #     print(i)
        try:
            i.encode('gbk')
 
            text +=i
        except:
            # print(i)
            pass
       
    return text


# In[ ]:


import random


# In[ ]:


#比较不同手机品牌的情感分析结果：
for shop in shops:
    print('店铺：',shop)
    data1 = data[data['店铺名称']==shop][['商品ID', '店铺名称']]
    data2 = pd.merge(cc,data1,left_on = 'url',right_on ='商品ID' )
    index = data2.index.to_list()
    random.shuffle(index)
    # 随机抽取500条分析
    data3 = data2.loc[index[:50]]
    pos = []
    negs = []
    scores = []
    errors = []
    for i in data3['评论']:
        i = del_emoji(i)
        result = client.sentimentClassify(i)
        try:
            score = result['items'][0]["positive_prob"]
            scores.append(score)
            # 好评
            if score>0.999:
                pos.append(i)
            if score<0.1:
                negs.append(i)
        except:
            errors.append(i)
    print('平均值：',np.mean(scores))
    print('中位数：',np.median(scores))
    print('好评占比：',len(pos)/50)
    print('差评占比：',len(negs)/50)


# In[ ]:


# 比较不同手机品牌的好评和差评的观点：
for shop in shops[:5]:
    print('店铺：',shop)
    data1 = data[data['店铺名称']==shop][['商品ID', '店铺名称']]
    data2 = pd.merge(cc,data1,left_on = 'url',right_on ='商品ID' )
    index = data2.index.to_list()
    random.shuffle(index)
    # 随机抽取500条分析
    data3 = data2.loc[index[:50]]
    pos = []
    negs = []
    scores = []
    errors = []
    for i in data3['评价内容(content)']:
        i = del_emoji(i)
        result = client.sentimentClassify(i)
        try:
            score = result['items'][0]["positive_prob"]
            scores.append(score)
            # 好评
            if score>0.999:
                pos.append(i)
            if score<0.1:
                negs.append(i)
        except:
            errors.append(i)
    print('平均值：',np.mean(scores))
    print('中位数：',np.median(scores))
    print('好评占比：',len(pos)/500)
    print('差评占比：',len(negs)/500)
    # 好评
# 好评分析
    print('好评观点')
    for i in pos:
        options = {}
        options["type"] = 13
        ops = client.commentTag(i, options)
        if len(ops['items'])!=0:
            for j in ops['items']:
                print(j['prop']+j['adj'])
    print('='*20)
# 差评 
    
    print('差评观点')
    for i in negs:
            options = {}
            options["type"] = 13
            ops = client.commentTag(i, options)
            if len(ops['items'])!=0:
                for j in ops['items']:
                    print(j['prop']+j['adj'])  
    print('+'*20)


# In[ ]:





# In[ ]:




