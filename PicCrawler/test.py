import requests
from bs4 import BeautifulSoup
import pymongo
import gridfs
import time

# 获取mongoClient对象
client = pymongo.MongoClient("localhost", 27017)
# 获取使用的database对象
db = client.test
# 获取图片存储集合
fs = gridfs.GridFS(db, "images")


def save_pic_to_disk():
    """
    将数据库中文件转存到本地文件系统
    :return: 无
    """
    fss = fs.find()
    for fl in fss:
        print(fl.md5)
        tp_file = open('d:/img/' + fl.md5 + '.jpg', "wb")
        tp_file.write(fl.read())
        tp_file.close()


def mongodb_delete(title, author):
    """
    根据小说标题和作者删除其小说封面信息
    例如：mongodb_delete('桃花扇','孔尚任')
    :param title 小说标题
    :param author 小说作者
    """
    record = db.novel.find_one({"title": title, "author": author})
    print(record)
    _id = record.get("_id")
    _img = record.get("imag")
    db.novel.remove({"_id": _id})
    fs.delete(_img)


def iterator(url):
    """
    遍历指定地址下的小说条目
    获取小说封面、标题和作者信息
    然后保存至数据库
    最后获取递归到下一页进行遍历
    :param url: 小说列表页面地址
    :return: 无返回
    """
    print(url)
    # 获取页面html，并使用beautifulsoup进行解析
    rs = requests.get(url).content.decode("gbk")
    bs_obj = BeautifulSoup(rs, "html.parser")
    content = bs_obj.find("div", {"id": "content"})
    # 获取小说列表，并遍历小说数据
    novels = bs_obj.findAll("div", {"class": "Sum Search_line"})
    for novel in novels:
        # 获取小说的名称、索引地址、作者
        name = novel.find("h2").find("a").get_text()
        index = novel.find("h2").find("a").get("href")
        author = novel.find("em").find("a").get_text()
        # 获取小说封面，并使用gridfs保存至mongo
        img = novel.find("img")
        rs = requests.get(img.get("src"))
        # 这种方式是将小说的题目等信息与封面图片保存在一起
        # fs.put(rs.content,title=name, author=author, url=index)
        # 这种方式进行保存图片文件，然后记录文件编号，比较像关系数据库的使用方式
        _id = fs.put(rs.content)
        db.novel.save(dict(title=name, author=author, url=index, imag=_id, time=time.time()))
    # 获取下一页链接，如果存在下一页就进行递归遍历
    next_page = content.find("div", {"id": "pagelink"}).find("a", {"class": "next"})
    if next_page:
        iterator(next_page.get("href"))


# 遍历全本小说网的小说信息
# 从小说站点的导航上可以看出，该站点小说分为11个类型，而且类型编号从1开始递增
for i in range(1, 12):
    iterator('http://www.wanbenxiaoshuo.net/sort/' + str(i) + '_1.html')
# 关闭资源
client.close()
