import time

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request


class Unsplash(object):
    # 初始化构造函数
    def __init__(self):
        self.count = 0
        self.tags = "sky"
        self.url = 'https://unsplash.com/search/photos/'
        self.save_path = "./unsplash/"
        self.driver = webdriver.Chrome('D:/chromedriver/chromedriver.exe')

    # 实现下拉动作，并返回网页源代码，times:下拉次数
    def do_scroll(self):
        # 打开目标网址
        driver = self.driver
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight*8/11);")
        target = driver.find_element_by_id("spinner")
        driver.execute_script("arguments[0].scrollIntoView();", target)

        # 解析网页源码
        html = driver.page_source
        return html

    # 下载图片保存到本地
    def save_img(self, src):
        t = time.time()
        img_name = str(int(round(t * 1000))) + ".jpg"
        print("保存的文件名字：" + img_name)
        try:
            urllib.request.urlretrieve(src, filename=self.save_path + img_name)
        except urllib.ContentTooShortError:
            print('Network conditions is not good.Reloading.')
            self.auto_down(src, img_name)

    def auto_down(self, url, filename):
        f = open(self.save_path + filename, 'wb')
        f.write((urllib.request.urlopen(url)).read())
        f.close()

    def get_pic(self, html):
        print(self.count)
        driver = self.driver
        soup = BeautifulSoup(html, "html.parser")
        soup_img_tmp = soup.findAll("img")
        print("len: " + str(len(soup_img_tmp)))
        if len(soup_img_tmp) == self.count:
            target = driver.find_elements_by_class_name("yVU8k")[-1]
            driver.execute_script("arguments[0].scrollIntoView();", target)
            time.sleep(10)

        soup_img = soup.findAll("img")[self.count:]
        self.count = self.count + len(soup_img)
        print(self.count)
        allImages = [x.get("src") for x in soup_img]
        images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x]
        # 获取图片下载地址，
        for url in images:
            if "photo" in url:
                self.save_img(url)

    def main(self):
        # 获取源码
        self.driver.get(self.url + self.tags)
        times = 20
        for i in range(times):
            print('正在下拉' + str(i + 1) + '次：')
            html = self.do_scroll()
            print('等待' + str(i + 1) + '次网页加载')
            time.sleep(10)
            print("开始下载图片")
            self.get_pic(html)

        self.driver.close()
