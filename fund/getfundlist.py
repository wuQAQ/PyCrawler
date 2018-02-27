# -*- coding:utf8 -*-
## 获取基金列表
import requests
import urllib.request 
from bs4 import BeautifulSoup
import time
import pandas as pd 
import codecs
import random
import json
import demjson
import csv

def randHeader():
    '''
    随机生成User-Agent
    :return:
    '''
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11',
                       'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0'
                       ]
    result = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
    }
    return result

def getCurrentTime():
        # 获取当前时间
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

def getURL(url, tries_num=5, sleep_time=0, time_out=10,max_retry = 5):
        '''
           这里重写get函数，主要是为了实现网络中断后自动重连，同时为了兼容各种网站不同的反爬策略及，通过sleep时间和timeout动态调整来测试合适的网络连接参数；
           通过isproxy 来控制是否使用代理，以支持一些在内网办公的同学
        :param url:
        :param tries_num:  重试次数
        :param sleep_time: 休眠时间
        :param time_out: 连接超时参数
        :param max_retry: 最大重试次数，仅仅是为了递归使用
        :return: response
        '''
        sleep_time_p = sleep_time
        time_out_p = time_out
        tries_num_p = tries_num
        try:
            res = requests.Session()
            if isproxy == 1:
                res = requests.get(url, headers=header, timeout=time_out, proxies=proxy)
            else:
                res = requests.get(url, headers=header, timeout=time_out)
            res.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        except requests.RequestException as e:
            sleep_time_p = sleep_time_p + 10
            time_out_p = time_out_p + 10
            tries_num_p = tries_num_p - 1
            # 设置重试次数，最大timeout 时间和 最长休眠时间
            if tries_num_p > 0:
                time.sleep(sleep_time_p)
                print (getCurrentTime(), url, 'URL Connection Error: 第', max_retry - tries_num_p, u'次 Retry Connection', e)
                return getURL(url, tries_num_p, sleep_time_p, time_out_p,max_retry)
        return res

def getFundList():
    try:
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=bzdm,asc&page=1,1&dt=1511800017933&atfc=&onlySale=1"
        res = getURL(url)
        startIdx = res.text.find("record:") + len("record:")
        endIdx = res.text.find(",pages:")
        records = res.text[startIdx:endIdx].strip('"')
    except Exception as e:
        print(getCurrentTime(), 'geturl', e)

    fund_list = []

    result = {}
    try:
        p_url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=bzdm,asc&page=1," + str(records) + "&dt=1511800017933&atfc=&onlySale=1"
        p_res = getURL(p_url)
        jsIdx = p_res.text.find('{')
        json_str = p_res.text[jsIdx:]
        jsonData = demjson.decode(json_str)
        fund_datas = jsonData["datas"]
        # print(fund_datas)
    except Exception as e:
        print(getCurrentTime(), 'get_page', e)

    fund_list = []
    i = 0
    for fund_data in fund_datas:
        i += 1
        result = {}
        print(fund_data)
        # fund_list.append(fund_data[0])
        result["fund_code"] = fund_data[0]
        result["fund_abbr_name"] = fund_data[1]
        result["nav"] = fund_data[3]
        result["add_nav"] = fund_data[4]
        result["pre_nav"] = fund_data[5]
        result["pre_add_nav"] = fund_data[6]
        result["day_growth"] = fund_data[7]
        result["day_growth_rate"] = fund_data[8]
        result["handling_charge"] = fund_data[17]
        print(i, "/", records, " ", result)
        fund_list.append(result)
    # print(fund_list)
    headers = ['fund_code', 'fund_abbr_name', 'nav', 'add_nav', 'pre_nav', 'pre_add_nav', 'day_growth', 'day_growth_rate', 'handling_charge']
    with open("XXX.csv","w",newline="") as datacsv:
        f_csv = csv.DictWriter(datacsv, headers)
        f_csv.writeheader()
        f_csv.writerows(fund_list)

def main():
    global sleep_time, header, isproxy
    header = randHeader()
    sleep_time = 0.1
    isproxy = 0
    getFundList()

main()