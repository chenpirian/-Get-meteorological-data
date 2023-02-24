import requests
import re
import time     
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from time import sleep


city_input = 'huangpi'  
year_input = 2022       #where and which year to get data
start=time.time()


"""

#url = 'https://www.tianqishi.com/chengshi/nianyueri.html'
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/110.0.1587.50",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
headers['User-Agent'] = random.choice(user_agent_list)
"""
#headers
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50' ,
            'cookie': '__bid_n=18655121eeff1125954207; FPTOKEN=imK4QH+yoGI3kFqanQGm1EFnqcK1Cm9GhGoXhsH5Ptl3AUnIDJ7aPN4I5GJIhHNJK9k3fwNlspo1E4aYNqNCxaSQyIWehjLOwug4RbJLoNFQ7CMRdsxgkoJiLVHwYwAAfDfJx6nZ9HXCv9HpmCKQgtQ6edcimB7TP4sr6jIaP5EHrrcBWHHfjJvOF2fph3Q3ZaYOQy4+TKK8kuAzghy4cIgMJghLTkQWm16sHa7Y9KR7JCQsDINHi1TUSq7JaADkrMU74BA0U4EMqQKyvjZfoKckY2RvvDKlYoU2lcFHr8K0p/AOCjxzPsWZ9L6uHo3/wIJhQdNMJahW4SaFiHxmUj0EEPTEshvRb/52HB0OeZ0EeXmZ7jw9yvbZFDXVFOiD/QY9yopqQiQvWWUNZaCKrA==|fx5OWsIfEQQ7t0GExD8Wd06MeLfuUJSzLF478xBMVrg=|10|5e361ea9861942a58e2cd86c3209a331; PHPSESSID=ktnoh1gci0nl48jaf6bpdvspr2; __51cke__=; Hm_lvt_40e6bcbf7e931ba5b8b2db344d6cd54f=1676795219,1676874598,1676966897,1676976332; __tins__19183526=%7B%22sid%22%3A%201676983428638%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201676985228638%7D; __51laig__=2; Hm_lpvt_40e6bcbf7e931ba5b8b2db344d6cd54f=1676983429'}

month_num = [1,3,5,7,8,10,12]
#month_num2 = [4,6,9,11]





def set_link(year):   
    link = []
    if (year % 4) == 0:    #闰平检测
        if (year % 100) == 0:
            if (year % 400) == 0:
                num_feb = 30
    else:
                num_feb = 29

    for i in range(1,13):
        if i == 2:
            if num_feb == 30:
                for j in range(1,30):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}020{}.html'.format(city_input,year,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}02{}.html'.format(city_input,year,j)
                    link.append(url)
            else:
                for j in range(1,29):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}020{}.html'.format(city_input,year,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}02{}.html'.format(city_input,year,j)
                    link.append(url)

        if i in month_num:
            if i < 10:
                for j in range(1,32):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}0{}0{}.html'.format(city_input,year,i,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}0{}{}.html'.format(city_input,year,i,j)
                    link.append(url)
            else:
                for j in range(1,32):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}{}0{}.html'.format(city_input,year,i,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}{}{}.html'.format(city_input,year,i,j)
                    link.append(url)

        else:
            if i < 10:
                for j in range(1,31):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}0{}0{}.html'.format(city_input,year,i,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}0{}{}.html'.format(city_input,year,i,j)
                    link.append(url)
            else:
                for j in range(1,31):
                    if j < 10:
                        url='https://www.tianqishi.com/{}/{}{}0{}.html'.format(city_input,year,i,j)
                    else:
                        url='https://www.tianqishi.com/{}/{}{}{}.html'.format(city_input,year,i,j)
                    link.append(url)
    return link

def get_page(url,headers):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        html.encoding = html.apparent_encoding
        return html.text
    else:
        return None

time_b = []
time_box = []
temp_b = []
wind_dir_b = []
wind_pow_b = []
wind_speed_b = []
presure_b = []
hunidity_b = []
rain_b = []


def get_data():
    link = set_link(year_input)
    day_num = 0
    for url in link:
        day_num = day_num + 1
        print(url)

        html = get_page(url,headers)
        bs = BeautifulSoup(html,'html.parser')

        data = bs.find_all('table')
        date = re.compile('width="22%">(.*?)</')
        wd_pre = re.compile('width="12%">(.*?)</')
        wp_ws_ra = re.compile('width="10%">(.*?)</')
        tem = re.compile('width="8%">(.*?)℃')
        hun = re.compile('width="9%">(.*?)</')
        
        time = re.findall(date,str(data))
        sample1 = re.findall(wd_pre,str(data))
        sample2 = re.findall(wp_ws_ra,str(data))
        sample3 = re.findall(hun,str(data))
        sample4 = re.findall(tem,str(data))

        #减缓爬取速度防止IP阻止
        #if (day_num % 5) == 0: 
            #sleep(1)
            #print('sleep 1.0s per 5 days')      


        
        #print(sample1)
        #print(sample2)
        #print(sample3)
        #print(sample4)
        #print(len(time))

        for i in range(len(time)):
            time2 = time[i]
            if i > 0 :
                time_b.append(time2)
        
       

        for i in range(len(time)):
            wd = sample1[i*2]
            pre = sample1[i*2+1]
            if i > 0 :
                wind_dir_b.append(wd)#风向
                presure_b.append(pre)#气压

        
        for i in range(len(time)):
            wp = sample2[i*3]
            ws = sample2[i*3+1]
            ra = sample2[i*3+2]
            if i > 0 :
                wind_pow_b.append(wp)#风力
                wind_speed_b.append(ws)#风速
                rain_b.append(ra)#降水概率
        

        for i in range(len(time)):
            hun = sample3[i]
            if i > 0 :
                hunidity_b.append(hun)#湿度
        

        for i in range(len(sample4)):
            temp = sample4[i]
            temp_b.append(temp)#温度



def Writedata(data):
    filename = city_input
   
    with open(filename,'w') as f: 
            f.write(str(data))
            f.close()



""""
print(len(wind_dir_b))
print(len(wind_pow_b))
print(len(wind_speed_b))
print(len(presure_b))
print(len(hunidity_b))
print(len(rain_b))
"""


get_data()

datas = pd.DataFrame({'time':time_b,'wind direction':wind_dir_b,'wind power':wind_pow_b,'wind speed':wind_speed_b,'presure':presure_b,'humidity':hunidity_b,'rain':rain_b,'temputure':temp_b})
#Writedata(datas)

datas.to_csv(city_input + 'data.txt', sep='\t',index=True, header = True,encoding='utf_8_sig')
#print(datas)


end=time.time()
print("Time Cost :{:.2f}".format(end-start))




