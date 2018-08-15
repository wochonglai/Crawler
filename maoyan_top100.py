# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
import re
import json
import time
import random
from multiprocessing import Pool
from multiprocessing import Manager
import functools


def get_one_page(url):
  # 获取一个页面数据
  headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
            }
  try:
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
      return response.text
    return None
  except RequestException:
    return None

