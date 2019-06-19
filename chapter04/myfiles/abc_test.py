# -*- coding: utf-8 -*-
from collections.abc import Sized
import abc


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company([1, 2, 3])
print(len(com))
# 某些情况下判断某个对象的类型
print(isinstance(com, Sized))

# *************************************************************** #
# 强制某个子类必须实现某些方法，设计一个抽象基类，指定子类必须实现某些方法
# class CacheBase():
#     def get(self):
#         raise NotImplemented
#
#     def set(self):
#         raise NotImplemented


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def set(self):
        pass


class RedisCache(CacheBase):
    def get(self):
        pass


"""
1.当CacheBase未继承abc.ABCMeta时，如果采用raise NotImplemented的方式，当RedisCache
初始化完成并且调用set方法时，才会发现这个set方法是必须实现的；
2.当CacheBase未继承abc.ABCMeta时，当初始化RedisCache类时就会报错，提示这个类没有实现
set方法，这样就避免了在调用时才知道方法没有被实现，避免了错误
"""
redis_cache = RedisCache()
redis_cache.set()


