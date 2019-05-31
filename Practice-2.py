#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

"""
Author: wangjf
date: 2019/5/31 17:20
desc:
"""
from collections import Iterable
from functools import reduce


def add(x, y):
	return x + y


reduce(add, [1, 3, 5, 7, 9])
isinstance([], Iterable)
