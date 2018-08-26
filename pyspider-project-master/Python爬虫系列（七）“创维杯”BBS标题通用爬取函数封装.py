
# coding: utf-8

# In[4]:


#标题普适性检查
#测试：标题是h1  #subjectTitle
import requests
from bs4 import BeautifulSoup
res01=requests.get('http://bbs.pcauto.com.cn/topic-12068997.html')
soup=BeautifulSoup(res01.text,'html.parser')
title=soup.select('h1')[0].text.strip()
len(soup.select('h1'))


# In[30]:


#测试02，这个标题是h2   \
#.bbs-title
res02=requests.get('http://bbs.mplife.com/showtopic-1324516.html')
soup=BeautifulSoup(res02.text,'html.parser')
title=soup.select('h1')[0].text.strip()
if len(title)<=0:
    title=soup.select('h2')[0].text.strip()
title
soup.select('.bbs-title h2')[0].text.strip()


# In[39]:


#测试03 h1 关键字 subject
res03=requests.get('http://bbs.lygbst.cn/forum.php?mod=viewthread&tid=4876466&extra=page%3D1%26filter%3Dsortid%26sortid%3D25')
soup=BeautifulSoup(res03.text,'html.parser')
title=soup.select('h1')[0].text.strip()
if len(title)<=0:
    title=soup.select('h2')[0].text.strip()
title


# In[62]:


#测试04 tr td   #msgsubject
res04=requests.get('http://bbs.jjwxc.net/showmsg.php?board=3&id=1019672')
res04.encoding='GBK'
soup=BeautifulSoup(res04.text,'html.parser')

title=soup.select('#msgsubject')[0]
title.text.strip().lstrip('主题：').rstrip('[102]')


# In[9]:


#测试05：h1 虎扑体育 .bbs-hd-h1 编码IOS
res05=requests.get('https://bbs.hupu.com/18904165.html')
#res05.encoding='utf-8'
soup=BeautifulSoup(res05.text,'html.parser')
title=soup.select('h1')[0].text.strip()
title
res05.encoding


# In[76]:


#测试06：华商论坛 h1 #subject_tpc
res06=requests.get('http://bbs.hsw.cn/read-htm-tid-18368990.html')
res06.encoding='utf-8'
soup=BeautifulSoup(res06.text,'html.parser')
title=soup.select('h1')[0].text.strip()
title


# In[21]:


#测试07：猴岛论坛 h1 #subject_tpc  GB2312  phpwind 出现不能获取页面内容
res07=requests.get('https://bbs.houdao.com/r13418976/')
soup=BeautifulSoup(res07.text,'html.parser')
#title=soup.select('h1')[0].text.strip()


# In[18]:


#和讯论坛  strong   空白 抓取失败
res08=requests.get('http://bbs.hexun.com/money/post_84_10765277_1_d.html')
res08.encoding='utf-8'
soup=BeautifulSoup(res08.text,'html.parser')

#title=soup.select('strong')[0].text.strip()


# In[112]:


#测试09：济南社区论坛 h1  #thread_subject  gbk
res08=requests.get('http://bbs.e23.cn/thread-180468227-1-1.html')

soup=BeautifulSoup(res08.text,'html.parser')
title=soup.select('h1')[0].text.strip()
title


# In[7]:


#测试10：时空网 h1 >a thread_subject
res10=requests.get('http://bbs.gxsky.com/thread-13665501-1-1.html')

soup=BeautifulSoup(res10.text,'html.parser')
#title=soup.select('h1')[0].text.strip()
soup.select('#thread_subject')[0].text


# In[8]:


#测试11：腾讯电脑管家  discuz  #thread_subject
res10=requests.get('http://bbs.guanjia.qq.com/forum.php?mod=viewthread&tid=5000457&extra=page%3D1')
soup=BeautifulSoup(res10.text,'html.parser')
soup.select('h1')[0].text.strip()


# In[3]:


s = 'text=cssPath:"http://imgcache.qq.com/ptlogin/v4/style/32",sig:"OvL7F1OQEojtPkn5x2xdj1*uYPm*H3mpaOf3rs2M",clientip:"82ee3af631dd6ffe",serverip:"",version:"201404010930"'
import re
res = re.findall(r'sig:"([^"]+)"',s)
res


# In[6]:


#获取标题函数封装
#所有提取论坛的地址
import requests
from bs4 import BeautifulSoup


def getTitle():
    url=input("请输入所需要的提取信息的bbs的url地址：\n")
    res=requests.get(url)
    #设置页面编码
    if res.encoding=='ISO-8859-1':
        res.encoding=='utf-8'
    #生成bs对象
    soup=BeautifulSoup(res.text,'html.parser')
    #判断阿抓取的页面是否为空
    if len(soup)==0:
        print('抓取页面失败')
    else:
        if len(soup.select('#thread_subject'))==0:
            print('标题的id不是thread_subject')        
            print('抓取标题失败')
        else:
            title=soup.select('#thread_subject')[0].text.strip()
            print(title)

getTitle()

