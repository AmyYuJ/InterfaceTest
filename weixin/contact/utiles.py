#!/usr/bin/env python
# encoding: utf-8

import pystache
import time

class Utiles:

    @classmethod
    def parse(self,template_path,dict):
        template = "".join(open(template_path).readlines())
        return pystache.render(template,dict)

    @classmethod
    def udid(cls):
        return str(time.time()).replace(".","")[0:11]