# -*- coding: utf-8 -*-

def getData():
    from lxml import etree
    import requests
    import csv
    import time

    # 写入 csv 文件                
    def saveToCsv(item, mode, file):
        with open(file, mode, encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            try:
                writer.writerow(item)
            except:
                print('write error')
    
    # 写入 txt 文件，用于词云分析
    def saveToTxt(world, mode, file):
        f = open(file, mode, encoding='utf-8')
        f.write(world)
        
    start_url = 'https://qd.anjuke.com/sale/p{}/?from=navigation'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
    '''
    header = ['court', 'house', 'area', 'u_price', 't_price', 'detail_url']
    # 重置文件用
    saveToCsv(header, 'w', file('anjuke_qingdao.csv'))
    saveToTxt('', 'w',file('house.txt'))
    saveToTxt('', 'w',file('court.txt'))    
    '''
    page_num = 50 #50
    for page in range(1, page_num+1):
        url = start_url.format(page)
        response_html = requests.get(url,headers=headers)
        time.sleep(1)
        selector = etree.HTML(response_html.text)
        
        layout_list = selector.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
        for layout in layout_list:
            court = layout.xpath('a/div[2]/div[1]/section/div[2]/p[1]/text()')[0]
            house = ''
            for i in range(1, 7):
                house += layout.xpath('a/div[2]/div[1]/section/div[1]/p[1]/span[{}]/text()'.format(i))[0]
            area = layout.xpath('a/div[2]/div[1]/section/div[1]/p[2]/text()')[0].strip().strip('㎡')
            u_price = layout.xpath('a/div[2]/div[2]/p[2]/text()')[0].strip('元/㎡')
            t_price = layout.xpath('a/div[2]/div[2]/p[1]/span[1]/text()')[0]
            detail_url = layout.xpath('a/@href')[0]
            item = [court, house, area, u_price, t_price, detail_url] 
            
            saveToCsv(item, 'a', file('anjuke_qingdao.csv'))
            saveToTxt(house+' ', 'a', file('house.txt'))
            saveToTxt(court+' ', 'a', file('court.txt'))
            print('正在抓取：',court)
        print("page {} finish".format(page))

def analysisData(filename):
    import pandas as pd
    data = pd.read_csv(file(filename),index_col=0)
    return data

def drawWordcloud(filename_txt,filename_png):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud

    with open(file(filename_txt),encoding='utf-8') as f:
        mytext = f.read()

    my_wordcloud = WordCloud(
        font_path='C://Windows/Fonts/simkai.ttf',
        background_color='white',
        width = 800,
        height = 600
        ).generate(mytext)
    plt.imshow(my_wordcloud, interpolation='bilinear')
    plt.axis("off")
    my_wordcloud.to_file(file(filename_png))

def drawPieOfPie(filename,data,filename_png):

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

    def printListt(list0,list1):
        for i in range(0,len(list0)):
            print('\t'+list0[i]+': ', list1[i])
    print('所有二手房每平方米价格分段统计如下：')
    printListt(listt00,listt01)
    print('对其中占比最大的 1w-2w 区间分段统计如下：')
    printListt(listt10,listt11)
    
    temp = listt00[1]
    listt00[1] = listt00[10]
    listt00[10] = temp
    temp = listt01[1]
    listt01[1] = listt01[10]
    listt01[10] = temp

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
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.03)    # 分裂距离

    ax1.pie(x=quantity,
            colors=['r', 'g', 'm', 'c', 'y', 'b', 'r', 'g', 'm', 'c', 'y'],
            explode=explode,
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

    plt.savefig(file(filename_png)) 


if __name__ == '__main__':
    filepath = 'D://Programming/Python/Spider'
    def file(filename):
        return filepath+'/'+filename
    getData()
    data = analysisData('anjuke_qingdao.csv')
    print(data.head)
    drawWordcloud('house.txt','housecloud.png')
    drawWordcloud('court.txt','courtcloud.png')
    drawPieOfPie('anjuke_qingdao.csv',data,'pie of pie.png')