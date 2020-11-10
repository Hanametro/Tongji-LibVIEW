# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import datetime,time
import csv
def timestamp_full(x):#换算时间戳到具体时间
    dateArray = datetime.datetime.fromtimestamp(x)
    return dateArray.strftime("%H:%M")

def main(area):
    plt.rcParams['figure.figsize']=(30,12)
    plt.rcParams['font.sans-serif']=['DengXian']
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid(True)
   # plt.rcParams['figure.dpi'] = 300

    if area==1:
        filename='data01.csv'
        areaname='四平路校区图书馆'
    elif area==2:
        filename='data02.csv'
        areaname='嘉定校区图书馆'
    else:
        pass
    
    timeList=[]
    numberList=[]
    tickList=[]
    with open(filename)as k:
        k_csv = csv.reader(k)
        for row in k_csv:       
            timeList.append(int(row[0]))
            numberList.append(int(row[1]))
            
    i=0
    for i in range(0,int(len(timeList)/3)):
        tickList.append(timeList[3*i])   
        i=i+1
            
    plt.title("["+areaname+"] 人数趋势图 ")
    plt.xlabel('时间')
    plt.ylabel('人数')
    plt.plot(timeList,numberList,marker='.')   
    plt.xticks(tickList,[timestamp_full(int(x)) for x in tickList])
    plt.show()
    plt.close()    
    numberMAX=max(numberList)
    MAXid=numberList.index(max(numberList))
    MAXtime=timestamp_full(timeList[MAXid])                       
    print(areaname,"最大人数出现在",MAXtime,"，人数：",numberMAX)     

                  
if __name__ == '__main__':
    main(1)
    main(2)
    
  