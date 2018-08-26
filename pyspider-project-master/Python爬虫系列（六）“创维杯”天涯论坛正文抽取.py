
# coding: utf-8

# In[61]:


#获取正文标题
import requests
from bs4 import BeautifulSoup
from datetime import datetime
res=requests.get('http://bbs.tianya.cn/post-stocks-1841155-1.shtml')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
soup.select('.s_title')[0].text.strip()


# In[75]:


time=soup.select('.atl-info')[0].select('span')[1].text.lstrip('时间：')
info=soup.select('.atl-info')[0].select('span')
uname=info[0].select('a')[0]['uname']
time=datetime.strptime(info[1].text.lstrip('时间：').strip(),'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
clickCounts=info[2].text.strip('点击：')
replyCounts=info[3].text.strip('回复：')


# In[77]:


#天涯论坛正文提取抽取函数
#获取正文标题
import requests
from bs4 import BeautifulSoup
from datetime import datetime
def getTYInfo(bbsurl):
    res=requests.get(bbsurl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    info=soup.select('.atl-info')[0].select('span')
    result={}
    result['replyCounts']=info[3].text.strip('回复：')
    result['clickCounts']=info[2].text.strip('点击：')
    result['time']=datetime.strptime(info[1].text.lstrip('时间：').strip(),'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    result['uname']=info[0].select('a')[0]['uname']
    result['title']=soup.select('.s_title')[0].text.strip()
    return result


# In[79]:


url='http://bbs.tianya.cn/post-funinfo-7418649-1.shtml'
getTYInfo(url)

