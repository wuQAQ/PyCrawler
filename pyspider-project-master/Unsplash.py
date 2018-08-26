from selenium import webdriver#ʵ���Զ�����
from lxml import etree#��λԪ�أ����Ӹ�Ч��
from urllib.parse import urlparse#����ͼƬ������
import urllib.request#urlretrieve()���ر���ͼƬ
import re
import time


class Unsplash:
    #��ʼ�����캯��
    def __init__(self):
        self.url='https://unsplash.com/'#�����ַ
        self.save_path="G://unsplash/"#ͼƬ����·��
        self.driver=webdriver.Chrome('G:/chromedriver/chromedriver.exe')
        #self.driver = webdriver.PhantomJS()
    #ʵ��������������������ҳԴ���룬times:��������
    def do_scroll(self,times):
        #��Ŀ����ַ
        driver=self.driver
        driver.get(self.url)
        #ģ����������
        for i in range(times):
            print('��������'+str(i+1)+'�Σ�')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('�ȴ�'+str(i+1)+'����ҳ����')
            time.sleep(40)
        #������ҳԴ��
        html=etree.HTML(driver.page_source)
        return html

    #����ͼƬ���浽����
    def save_img(self,src,img_name):
        urllib.request.urlretrieve(src, filename=self.save_path + img_name)

    def get_pic(self, html):

        #��ȡa��ǩ��style����
        all_uls = html.xpath('//a[@class="cV68d"]/@style')
        # ��ȡͼƬ���ص�ַ��
        for url in all_uls:
            #ʹ��������ʽ��ȡ��Ҫ��src��ַ
            src = re.findall(r'url\(\"(.*?)\"\)',url,re.S)[0]
            print(src)
            #ʹ��urlparse������ַ��ʹ��path�����ݣ�ȥ������Ҫ�Ĳ���
            fina_src=urlparse(' ' + src).path.strip()
            # ����ͼƬ������
            img_name = fina_src.split('/')[-1]+'.jpg'
            print(fina_src,img_name)
            self.save_img(src,img_name)

    def main(self):
        #��ȡԴ��
        html=self.do_scroll(1)
        print("��ʼ����ͼƬ")
        self.get_pic(html)
img=Unsplash()
img.main()