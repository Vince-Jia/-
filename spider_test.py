# -*- coding: utf-8 -*-
'''
import pandas as pd

filename = 'D://Programming/Python/Spider/anjuke_qingdao.csv'
data = pd.read_csv(filename,index_col = 0)
print(data)
print(data['house'])

filename = 'D://Programming/Python/Spider/House.txt'
with open(filename, 'a', encoding='utf-8')
'''

'''
import requests
from lxml import etree
url = 'https://qd.anjuke.com/sale/p1/?from=navigation'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
r = requests.get(url, headers=headers)
selector = etree.HTML(r.text)
layout_list = selector.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
for layout in layout_list:    
    house = ''
    for i in range(1, 7):
        house += layout.xpath('a/div[2]/div[1]/section/div[1]/p[1]/span[{}]/text()'.format(i))[0]
    print(house)
 '''

''' 
from wordcloud import wordcloud
from PIL import Image
file = 'D://Programming/Python/Spider/HouseCloud.txt'
with open(file, encoding='utf-8') as f:
    text = f.read()

import jieba
def trans_CN(text):
    word_list = jieba.cut(text)
    result = ' ',jion(word_list)
    return result

wordcloud = WordCloud(
    font_path = 'D://Programming/Python/Spider/House.TTF'
    ).generate(text)
image_produce=wordcloud.to_image()
image_produce.show()
'''
'''
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = 'D://Programming/Python/Spider/HouseCloud.txt'
with open(file,encoding='utf-8') as f:
    mytext = f.read()
#text_from_file_with_apath = open(file, encoding='utf-8').read(mytext)

my_wordcloud = WordCloud(font_path='C://Windows/Fonts/STCAIYUN.TTF').generate(mytext)
#%pylab inline
plt.imshow(my_wordcloud, interpolation='bilinear')
plt.axis("off")

my_wordcloud.to_file('D://Programming/Python/Spider/HouseCloud.jpg')
'''
'''
def saveToTxt(item, mode, filename):
    with open(filename, mode, encoding='utf-8') as f:
        f.write(item)
        
filename = 'D://Programming/Python/Spider/testt.txt'
saveToTxt('', 'w', filename)
for strr in ['123', '465', '789']:
    saveToTxt(strr, 'a', filename)
'''
'''
import requests
from lxml import etree
url = 'https://qd.anjuke.com/sale/p1/?from=navigation'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
r = requests.get(url, headers=headers)
selector = etree.HTML(r.text)

layout1 = '//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]'
court = selector.xpath('a/div[2]/div[1]/div[1]/h3/@title')
print(court)
'''
'''
import requests
import time
start_url = 'https://qd.anjuke.com/sale/p{}/?from=navigation'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
'''
'''
page_num = 5 #50
for page in range(1,page_num+1):
    url = start_url.format(page)
    print(url)
    response_html = requests.get(url,headers=headers)
    time.sleep(1)
    print(response_html.text)
    print('*'*20,'page {} finish'.format(page),'*'*20)
'''
'''
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

data_df = pd.read_csv('anjuke_qingdao.csv')
df = data_df.dropna()
df1 = df[['court', 'u_price']]
df2 = df1.iloc[:20]
print(df2['court'].values)
print(df2['u_price'].values)

#数据分析代码
c = 
    Bar()
        .add_xaxis(list(df2['court'].values))
        .add_yaxis("u_price", list(df2['u_price'].values))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="成交量图表 - Volume chart"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("data.html")
)
print('数据可视化结果完成,请在当前目录下查找打开 data.html 文件!')
'''
'''
import pandas as pd
data = pd.read_csv('anjuke_qingdao.csv',index_col=0)
print(data['u_price'])
listt0 = ['1w以下', '1w-2w', '2w-3w', '3w-4w', '4w-5w', '5w-6w', '6w-7w', '7w-8w', '8w-9w', '9w-10w', '10w及以上']
listt1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
for i in data['u_price']:
    print(i)
    if i >= 100000:
        listt1[10] += 1
        print("10w+")
    else:
        for j in range(0,10):
            if i < (j+1)*10000:
                listt1[j] += 1
                print('{}w-{}w'.format(j, j+1))
                break
    print('\n')
print(listt1)    
'''
  

## important

import pandas as pd
data = pd.read_csv('anjuke_qingdao.csv',index_col=0)

listt00 = ['1w以下', '1w-2w', '2w-3w', '3w-4w', '4w-5w', 
           '5w-6w', '6w-7w', '7w-8w', '8w-9w', '9w-10w', '10w及以上']
listt01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
listt10 = ['1w-1.1w', '1.1w-1.2w', '1.2w-1.3w', '1.3w-1.4w', '1.4w-1.5w', 
           '1.5w-1.6w', '1.6w-1.7w', '1.7w-1.8w', '1.8w-1.9w', '1.9w-2w']
listt11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in data['u_price']:
    if i >= 100000:
        listt01[10] += 1
    else:
        for j in range(0,10):
            if i < (j+1)*10000:
                listt01[j] += 1
                if j+1 == 2:
                    i -= 10000
                    for k in range(0,11):
                        if i < (k+1)*1000:
                            listt11[k] += 1
                            break
                break

temp = listt00[1]
listt00[1] = listt00[10]
listt00[10] = temp
temp = listt01[1]
listt01[1] = listt01[10]
listt01[10] = temp
print(listt00)
print(listt01)
print(listt10)
print(listt11)

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
# 使图表元素中正常显示中文
mpl.rcParams['font.sans-serif'] = 'SimHei'
# 使坐标轴刻度标签正常显示负号
mpl.rcParams['axes.unicode_minus'] = False

# 画布
fig = plt.figure(figsize=(12, 6),
                 facecolor='cornsilk'
                )
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace=0)

# 定义数据
data = {'category': listt00,
        'quantity': listt01
       }

others = {'category': listt10,
          'quantity': listt11
         }

# 大饼图
labs = data['category']
quantity = data['quantity']
explode = (0, 0, 0, 0, 0, 0.03)    # 分裂距离

ax1.pie(x=quantity,
        colors=['r', 'g', 'm', 'c', 'y', 'b', 'r', 'g', 'm', 'c', 'y'],
        #explode=explode,
        autopct='%1.1f%%',
        startangle=70,
        labels=labs,
        textprops={'color': 'k',
                   'fontsize': 12,
                  }
       )

# 小饼图
labs2 = others['category']
quantity_2 = others['quantity']

ax2.pie(x=quantity_2,
        colors=['khaki', 'olive', 'gold', 'khaki', 'olive', 'gold', 'khaki', 'olive', 'gold'],
        autopct='%1.1f%%',
        startangle=70,
        #labels=labs2,
        radius=0.5,
        labels=labs2,
        shadow=True,
        textprops={'color': 'k',
                   'fontsize': 12,
                  },
       )

# 用 ConnectionPatch 画出两个饼图的间连线
## 饼图边缘的数据
theta1 = ax1.patches[-1].theta1
theta2 = ax1.patches[-1].theta2
center = ax1.patches[-1].center
r = ax1.patches[-1].r

width=0.2
# 上边缘的连线
x = r*np.cos(np.pi/180*theta2)+center[0]
y = np.sin(np.pi/180*theta2)+center[1]
con_a = ConnectionPatch(xyA=(-width/2,0.5), xyB=(x,y),
                        coordsA='data', coordsB='data',
                        axesA=ax2, axesB=ax1
                       )

# 下边缘的连线
x = r*np.cos(np.pi/180*theta1)+center[0]
y = np.sin(np.pi/180*theta1)+center[1]
con_b = ConnectionPatch(xyA=(-width/2,-0.5), xyB=(x,y),
                        coordsA='data', coordsB='data',
                        axesA=ax2, axesB=ax1
                       )

for con in [con_a, con_b]:
    con.set_linewidth(1)    # 连线宽度
    con.set_color=([0,0,0])    # 连线颜色
    ax2.add_artist(con)   # 添加连线\
