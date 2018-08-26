
# coding: utf-8

# In[10]:


import requests,re
#打开网页获取源码
def get_content():
    url='http://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    res=requests.get(url)
    res.encoding='gbk'
    print(res.text)
get_content()


# In[11]:


def get():
    html=get_content()
    pattern=re.compile(r'')
    


# In[13]:


html='<div class="el"><p class="t1 "><input class="checkbox" type="checkbox" name="delivery_jobid" value="88007506" jt="0" /><span><a target="_blank" title="Python爬虫开发工程师" href="http://jobs.51job.com/chengdu-whq/88007506.html?s=01&t=0" onmousedown="">Python爬虫开发工程师 </a></span></p><span class="t2"><a target="_blank" title="成都易屋之家科技有限公司" href="http://jobs.51job.com/all/co3649202.html">成都易屋之家科技有限公司</a></span><span class="t3">成都-武侯区</span><span class="t4">0.8-1.5万/月</span><span class="t5">04-21</span></div>'
reg=re.compile(r'class="t1 ">.*?')

