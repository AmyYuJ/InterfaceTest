#!/usr/bin/env python
# encoding: utf-8

from weixin.contact.user import User
from weixin.contact.utiles import *
import time
import logging

class TestUser:

    depart_id=65

    @classmethod
    def setup_class(cls):
        cls.user = User

    def test_create(self):
        uid = "amy"+str(time.time())
        data={
            "userid": uid,
            "name": uid,
            "department": self.depart_id,
            "email": uid+"@testerhome.com"
        }
        r = self.user.create(data)
        logging.info(r)
        assert r["errcode"]==0

    def test_create_by_template(self):   # 模板替换字段创建
        uid = "amy"+str(time.time())
        mobile = Utiles.udid()
        data=str(Utiles.parse("user_create.json",{
            "name": uid,
            "title": "校长",
            "email": mobile+"@qq.com",
            "mobile": mobile
        }))
        data = data.encode("utf-8")
        r = self.user.create(data)
        logging.info(r)
        assert r["errCode"] == 0

    def test_list(self):
        r = self.user.list()
        logging.info(r)

        r = self.user.list(department_id=65)
