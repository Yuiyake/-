# -*- coding = utf-8 -*-
# @Time : 2021/11/10 9:21
# @Author : 孙誉瑛
# @File : catch.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import requests
import time
import pymysql
import matplotlib.pyplot as plt


# 配置header，配置referer防盗链防止图片爬不下来
headers = {
    # 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.3; .NET4.0C; .NET4.0E)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f',
    'Connection': 'keep-alive'}
page = ('pg')

def generate_cityurl(user_in_city):  # 生成url
    cityurl = 'https://' + user_in_city + '.lianjia.com/loupan/'
    return cityurl
    # return demjson.encode(res)

def areainfo(url):
    page = ('pg')
    for i in range(1, 2):  # 获取1-n页的数据
        if i == 1:
            i = str(i)
            a = (url + page + i + '/')
            r = requests.get(url=a, headers=headers)
            print(a)
            htmlinfo = r.content
        else:
            i = str(i)
            a = (url + page + i + '/')
            print(a)
            r = requests.get(url=a, headers=headers)
            html2 = r.content
            htmlinfo = htmlinfo + html2
            # htmlinfo = html2
    time.sleep(0.2)
    return htmlinfo

hlist = []
def listinfo(listhtml):
    areasoup = BeautifulSoup(listhtml, 'html.parser')
    ljhouse = areasoup.find_all('div', attrs={'class': 'resblock-desc-wrapper'})
    # print(areasoup)
    loupanimg = areasoup.find_all("img", attrs={"class": "lj-lazy"})
    i=0
    for house in ljhouse:
        loupantitle = house.find("div", attrs={"class": "resblock-name"})
        loupanname = loupantitle.a.get_text()
        loupantag = loupantitle.find_all("span")
        wuye = loupantag[0].get_text()
        xiaoshouzhuangtai = loupantag[1].get_text()
        location = house.find("div", attrs={"class": "resblock-location"}).get_text()
        jishi = house.find("a", attrs={"class": "resblock-room"}).get_text()
        area = house.find("div", attrs={"class": "resblock-area"})
        sarea = area.find("span").get_text()
        # print(sarea)
        r_area = '暂无'
        if sarea != '':
            r_area = house.find("div", attrs={"class": "resblock-area"}).get_text().split()[1]
        tag = house.find("div", attrs={"class": "resblock-tag"}).get_text()
        jiage = house.find("div", attrs={"class": "resblock-price"})
        price = jiage.find("div", attrs={"class": "main-price"}).get_text().split()[0]  # 截取数字
        if price.replace('\n','').find('-') != -1:
           price = price.split('-')[1]
        total = jiage.find("div", attrs={"class": "second"})
        totalprice = "暂无"
        if total is not None:
            totalprice = total.get_text()
        h = {'title': loupanname, 'wuye': wuye, 'states': xiaoshouzhuangtai, 'location': location.replace("\n", ""),
             'jishi': jishi.replace("\n", ""), 'area': r_area.replace('\n', ''), 'tag': tag.replace('\n', ''), 'price': price.replace('\n', ''),
             'totalprice': totalprice,'loupanimg':loupanimg[i].get('data-original')};
        i = i+1
        hlist.append(h)

# 下载图片到本地
def downloadPic(hlist):
    for i in range(len(hlist)):
        imgUrl = requests.get(hlist[i]['loupanimg']).content
        f = open('C:\\Users\\Lenovo\\Desktop\\study\\py\\catchLJ\\imgFile\\'+hlist[i]['title']+'.jpg', 'wb')
        f.write(imgUrl)
        print(hlist[i]['title'], "图片正在下载")
    print("图片下载完成")
    f.close()

# 可视化
def printPic(list):
    plt.rcParams["font.family"] = "kaiti"
    priceData = []
    lowNum = 0
    midNum = 0
    heighNum = 0
    # 数据准备
    for i in range(len(list)):
        priceData.append(int(list[i]['price']))
    # print(priceData)
    for num in priceData:
        if num <= 20000:
            lowNum = lowNum + 1
        elif num <= 45000:
            midNum = midNum + 1
        else:
            heighNum = heighNum + 1
    p_low = lowNum / len(priceData)
    p_mid = midNum / len(priceData)
    p_height = heighNum / len(priceData)
    # print(p_low, p_mid, p_height)
    nums = [p_low, p_mid, p_height]
    labels = ['0-20000', '20001-45000', '>45000']
    # 用Matplotlib画饼图
    plt.pie(x=nums, labels=labels, autopct="%.1f%%", shadow=True)
    plt.title('楼价区间比例(每平)', size=20)
    plt.show()


if __name__ == '__main__':
    # user_in_city = input('输入抓取城市：')
    user_in_city = 'gz'
    url = generate_cityurl(user_in_city)
    print(url)
    areahtml = areainfo(url)
    listinfo(areahtml)
    downloadPic(hlist)
    printPic(hlist)

    # print(hlist)
    for row in hlist:
        print(row)
    # for i in range(len(hlist)):
    #     # print(hlist[i]['title'])
    #     for key in hlist[i]:
    #         print(hlist[i][key])

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='catchdata',
    charset='utf8',
    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
for i in range(len(hlist)):
    try:
        insert_sql = "insert into gzdata(title, wuye, states, location, jishi, area, tag, price, totalprice, imgurl) values ("
        for key in hlist[i]:
            insert_sql = insert_sql + "'" + hlist[i][key] + "',"
        insert_sql = insert_sql[:-1] + ")"
        # print(insert_sql)
        cursor.execute(insert_sql)
        conn.commit()
    except:pass
print("数据入库完成")
# 关闭数据库连接
conn.close()



# sql_create = "CREATE TABLE `gzdata`  (`title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`wuye` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`states` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`jishi` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`area` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`tag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`totalprice` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,`imgurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;"
# print("创建数据库成功")