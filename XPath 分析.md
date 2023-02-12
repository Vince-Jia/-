# 一、网页爬取
## HTML
### headers
```python
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
```
### WebPage
Page1: https://qd.anjuke.com/sale/?from=navigation

Page2: https://qd.anjuke.com/sale/p2/?from=navigation

**Page{}: https://qd.anjuke.com/sale/p{}/?from=navigation**
## XPath
### layout
layout1:  
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]``

layout2:  
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[2]``

**layout_list:  
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div``** 

### in layout1:
#### court
page1:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[2]/p[1]/text()``**  
page5:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[2]/p[1]``**


#### house
room:  
page1:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[1]/p[1]/span[1]``**   
page5:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[1]/p[1]/span[1]``**

hall:  
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[1]/p[1]/span[3]``**

toilet:  
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[1]/section/div[1]/p[1]/span[5]``**

#### area
page1:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]``
**``/a/div[2]/div[1]/section/div[1]/p[2]``**   
page5:``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]``
**``/a/div[2]/div[1]/section/div[1]/p[2]``**

#### unit_price
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[2]/p[2]``**   
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[2]/p[2]``**

#### total_price
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[2]/p[1]/span[1]``**   
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a/div[2]/div[2]/p[1]/span[1]``**

#### detail_url
``//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[1]/``
**``a``**

# 二、文本分析

# 三、可视化