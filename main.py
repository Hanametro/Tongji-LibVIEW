# -*- coding: utf-8 -*-
import requests
import time,datetime
from bs4 import BeautifulSoup
import csv

def main():
    hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    url2="https://www.lib.tongji.edu.cn/"
    r1 = requests.get(url2,headers=hd)
    soup = BeautifulSoup(r1.text, 'html.parser')
    place_list = soup.find_all('span', class_='where')
    number_list = soup.find_all('label', class_='focus')
    capacity_list=[3153,2800]
    list1=[]
    list2=[]
    
    for item in place_list:    

        a=item.text
        list1.append(a)
    
    for item in number_list:   
        try:
            a=int(item.text)
            list2.append(a)    
        except:
            pass
    nowTime=int(time.time())
    print("当前时间：",datetime.datetime.now().strftime('%m-%d %H:%M:%S'))
    for i in range(0,2):
        print(list1[i],str(list2[i])+"/"+str(capacity_list[i]),'%.2f'%(list2[i]/capacity_list[i]*100))
      
    data1 = [(nowTime,list2[0])]
    data2= [(nowTime,list2[1])]
    f = open('data01.csv','a',newline='\n')
    writer = csv.writer(f)
    for k in data1:
        writer.writerow(k)
    f.close()
    f2 = open('data02.csv','a',newline='\n')
    writer = csv.writer(f2)
    for k in data2:
        writer.writerow(k)
    f2.close()  
while True:
    try:
        main()
        time.sleep(60)
    except:
        print('获取失败')
        time.sleep(30)