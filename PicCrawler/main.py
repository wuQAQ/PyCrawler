from pprint import pprint

from Browser.Unsplash import Unsplash
from Browser.MongoCURD import Connect

if __name__ == "__main__":
    img = Unsplash()
    img.main()
    # client = Connect.get_connection()
    # # 连接到数据库myDatabase
    # db = client.wuqaq
    # cursor = db.inventory.find({})
    # for inventory in cursor:
    #     pprint(inventory)
