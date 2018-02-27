import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def fillFundList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find(id='oTable').tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[1].string, tds[2].string, tds[3].a.string, tds[4].string, tds[5].string, 
                        tds[6].string, tds[7].string, tds[8].string, tds[9].string])

def printFundList(ulist, num):
    tplt = "{0:^5}\t{1:^5}\t{2:{9}^10}\t{3:^5}\t{4:^5}\t{5:^5}\t{6:^5}\t{7:^5}\t{8:^5}"
    print(tplt.format("序号", "基金代码", "名称", "估算值", "估算增长率", "单位净值", "日增长率", "估算偏差", "前单位净值", chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], chr(12288)))

def main():
    uinfo = []
    url = 'http://fund.eastmoney.com/fundguzhi.html'
    html = getHTMLText(url)
    fillFundList(uinfo, html)
    printFundList(uinfo, 100)

main()