#!/usr/bin/env python
# encoding: utf-8
import requests
import logging
import json
import jsonpath
from hamcrest import *
from jsonschema import validate

class TestRequests:

    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r = requests.get(url=self.url)
        logging.info(r)   # INFO:root:<Response [200]>
        logging.info(type(r))  # INFO:root:<class 'requests.models.Response'>
        logging.info(r.text)  # INFO:root:{"topics":[{"id":22722,"title":"\u003c新人...
        logging.info(type(r.text))  # INFO:root:<class 'str'>
        logging.info(r.json())  # INFO:root:{'topics': [{'id': 22722, 'title': '<新人问好> 我为
        logging.info(type(r.json())) # INFO:root:<class 'dict'>
        logging.info(json.dumps(r.json(),indent=2))  #INFO:root:{
                                                          # "topics": [
                                                          #   {
                                                          #     "id": 22722,
                                                          #     "title": "<\u65b0\u4eba\u95ee\u597d> \u6211\u4e3a\u4f55\u8981\u653e\u5f03 [\u524d\u7aef] \u8f6c\u5c97\u5230\u6d4b\u8bd5\uff1f\u5168\u56e0\u4ed6\u7684\u4e00\u53e5\u8bdd\uff01",
                                                          #     "created_at": "2020-03-28T16:19:22.981+08:00",
                                                          #     ...
        logging.info(type(json.dumps(r.json(),indent=2)))  # INFO:root:<class 'str'>

    def test_get_params(self):
        r = requests.get(url=self.url,
                          params = {"a":1,"b":"string content"},
                          headers = {"a":"1","b":"b2"},
                          proxies = {"https":"https://127.0.0.1:8888",
                                     "http":"http://127.0.0.1:8888"},
                          verify = False)
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_cookies(self):
        r = requests.get("http://httpbin.org/cookies",cookies = {"a":"1","b":"string content"})
        logging.info(r.text)

    def test_xueqiu_quote(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?"
        r = requests.get(url=url,
                         params={"category":"2"},
                         headers={"User-Agent":"Xueqiu Android 11.19"},
                         cookies={"u":"3446260779","xq_a_token":"5806a70c6bc5d5fb2b00978aeb1895532fffe502"})
        logging.info(json.dumps(r.json(),indent=2))
        assert r.json()["data"]["category"]==2
        assert r.json()["data"]["stock"][0]["name"]=="华宝中短债债券C"
        assert jsonpath.jsonpath(r.json(),"$.data.stocks[?(@.symbol=='F006947')].name")[0]=="华宝中短债债券A"
        assert_that(jsonpath.jsonpath(r.json(),"$.data.stocks[?(@.symbol=='F006947')].name")[0],equal_to("华宝中短债债券B"),"比较上市代码的名字")

    def test_xueqiu_list_schema(self):
        url = "https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json"
        r = requests.get(url=url,
                         params={"category": "2"},
                         headers={"User-Agent": "Xueqiu Android 11.19"},
                         cookies={"u": "3446260779", "xq_a_token": "5806a70c6bc5d5fb2b00978aeb1895532fffe502"})
        logging.info(json.dumps(r.json(), indent=2))

        schema=json.load(open("list_schema.json"))
        validate(instance=r.json(),schema=schema)

    def test_hamcrest(self):
        assert_that(0.1*0.1,close_to(0.01,0.0000000001))
        # assert_that(0.1 * 0.1, close_to(0.01, 0.000000000000000001))
        assert_that(["a","b","c"],all_of(has_items(["c","d"])))  # false
        assert_that(["a","b","c"],all_of(has_items(["c","b"])))  # true


