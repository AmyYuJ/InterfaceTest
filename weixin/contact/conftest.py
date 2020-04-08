#!/usr/bin/env python
# encoding: utf-8
import pytest
from weixin.contact.token import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_token_new()

# pytest.fixture标识，定义在函数前面.
# 在你编写测试函数的时候，你可以将此函数名称做为传入参数，pytest将会以依赖注入方式，将该函数的返回值作为测试函数的传入参数。
# 我们可以把fixture看做是资源，在你的测试用例执行之前需要去配置这些资源，执行完后需要去释放资源。适合于那些许多测试用例都只需要执行一次操作。