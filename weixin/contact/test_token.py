#!/usr/bin/env python
# encoding: utf-8

import logging
from weixin.contact.token import Weixin


class TestToken:

    logging.basicConfig(level=logging.DEBUG)

    def test_token(self):
        logging.info(Weixin.get_token())
        assert Weixin.get_token() != ""


