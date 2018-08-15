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

 def deal_one_page(html):
  pattern = re.compile('<p class="name">[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p '
                        'class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
  results = re.findall(pattern,html)
  #resultsL = []
  for item in results:
     # print(item[0],item[1],item[2])
     # resultsL.append({'title':item[0].strip(),
     #                  'stars':item[1].strip(),
     #                  'releasetime':item[2].strip()
     #                  })
  # return resultsL
     yield{
       'title':item[0].strip(),
       'stars':item[1].strip(),
       'releasetime':item[2].strip()
     }

def write2File(item):
  """
  将抓取到数据一条条写入maoyan.txt
  """
  with open("maoyan4.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps(item, ensure_ascii=False) + '\n')

def crawlPage(lock,offset):
  # 得到真正的URL
  url = "http://maoyan.com/board/4?offset="+str(offset)
  # 下载页面
  html = get_one_page(url)
  # 提取信息,写入到本地文件系统或者数据库
  for item in deal_one_page(html):
    lock.acquire()
    write2File(item)  # 将数据写到本地的文件系统中
    lock.release()


if __name__ == "__main__":
  #    for i in range(10):
  #        crawlPage(i*10)
  #        time.sleep(random.randint(1,3))#每抓取一个页面随机休息1到3秒钟
  manager = Manager()
  lock = manager.Lock()
  # 使用一个函数包装器
  pcrawlPage = functools.partial(crawlPage, lock)
  pool = Pool()
  pool.map(pcrawlPage, [i * 10 for i in range(10)])  # 分配给进程池任务序列
  pool.close()
  pool.join()

  print("Finished")
