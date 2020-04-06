#!/usr/bin/env python
# encoding: utf-8

import logging
import yaml
import requests

class Weixin:

    logging.basicConfig(level=logging.DEBUG)
    _token = ""
    @classmethod
    def get_token(cls):

        if len(cls._token)==0:
            cls._token=cls.get_token_new()
        return cls._token

    @classmethod
    def get_token_new(cls):
      conf = yaml.safe_load(open("/Users/yujing/testWorkspace/PycharmProjects/interfaceTest/weixin/contact/weixin.yaml"))
      logging.info(conf["env"])

      r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                       params={"corpid":conf["env"]["corpid"],
                               "corpsecret":conf["env"]["secret"]}).json()
      return r["access_token"]