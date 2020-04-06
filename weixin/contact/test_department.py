#!/usr/bin/env python
# encoding: utf-8

import time
import requests
import logging
import pytest
from weixin.contact.utiles import Utiles

class TestDepartment:

    def test_create_department_depth(self,token):

        parent_id = 1

        for i in range(14):
            data={
                "name": "amy"+str(parent_id)+str(time.time()),
                "parentid": parent_id
            }

            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                             params={"access_token": token},
                             json=data).json()
            logging.info(r)
            parent_id = r['id']

            assert r["errcode"] == 0

    @pytest.mark.parametrize("name",[
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self,name,token):
        data={
            "name": name+Utiles.udid(),
            "parentid": 1,
            "order": 1
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                         params={"access_token",token},
                         json=data).json()
        assert r["errcode"]==0