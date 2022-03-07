# -*- coding:utf-8 -*-
# @Time   :2022/2/28 5:08 下午
# @Author :Li Meng qi
# @FileName:extract_author.py
from extract_entity import BaseExtract
from entity.author import Author
import json

class ExtractAuthor(BaseExtract):
    def __init__(self):
        self.author = Author()

    def extract(self, row_data):
        # 这里就写一些对传过来的数据解析与特征建设的代码
        author_data = row_data['author']
        self.author.id = str(author_data['uid'])  # 作者id
        self.author.name = author_data['name']  # 作者名字
        self.author.user_type = author_data['user_type']  # 作者类型
        self.author.description = author_data['description']  # 作者简介
        self.author.is_advertiser = str(author_data['is_advertiser'])  # 是否是企业账号
        self.author.headline = author_data['headline']  # 作者的大字标题
        try:
            self.author.badge = json.dumps({'badge': author_data['badge']})  # 作者的徽章
        except Exception as e:
            print('author中不存在badge建')
            print(e)
            self.author.badge = json.dumps({'badge': []})  # 既然没有就赋值为空列表
        self.author.gender = str(author_data['gender'])  # 作者的性别
        self.author.url = author_data['url']  # 作者的主页链接
        self.author.url_token = author_data['url_token']  # 作者主页url唯一标识
        self.author.avatar_url = author_data['avatar_url']  # 作者头像的链接
        return self.author
