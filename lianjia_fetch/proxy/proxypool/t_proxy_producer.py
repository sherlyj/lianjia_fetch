#! -*- encoding:utf-8 -*-
import logging
from logging.config import fileConfig
from bs4 import BeautifulSoup as Bs
from xici_proxy_crawler import XiciProxyCrawler
from mock_proxy_crawler import MockIPCrawler
from thread_safe_set import LockedSet
from proxy_producer import ProxyProducer
from pool import ProxyPool


fileConfig("log-conf.ini")
logger = logging.getLogger("debugLog")

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,fr-FR;q=0.6,fr;q=0.4,en-US;q=0.2,en;q=0.2',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

crawler = MockIPCrawler(url='localhost', headers=headers)
pool = ProxyPool(crawler=crawler, maxSize=20)

producer = ProxyProducer(event=None,pool=pool, name="Producer1")
producer.start()

producer.join()

