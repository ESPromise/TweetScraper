
[![Build Status](https://travis-ci.org/ESPromise/TweetScraper.svg?branch=master)](https://travis-ci.org/ESPromise/TweetScraper)
[![Coverage Status](https://coveralls.io/repos/github/ESPromise/TweetScraper/badge.svg?branch=master)](https://coveralls.io/github/ESPromise/TweetScraper?branch=master)
[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/ESPromise/TweetScraper)

# tweet_scraper
用来爬取指定author的tweets爬虫
author列表: ./tweet_scraper/spiders/authors

run spider: scrapy crawl twitter

Pipeline选择：(setting.py中配置ITEM_PIPELINES)
1. SaveToFilePipeline(将爬取的数据以文件形式输出)
2. SaveToMongoPipeline(将爬取的数据直接存入mongodb，逻辑待开发)

DownloadMiddleWare选择: (setting.py中配置DOWNLOAD_MIDLEWARES)
1. scrapy_fake_useragent.middleware.RandomUserAgentMiddleware(开源库，用户随机从线上数据库中读取不同的header，需先用pip安装)


# requirements.txt
1. scrapy: 爬虫框架
2. pymongo: python 连接 mongodb 库
3. scrapy-fake-useragent: useragent faker库


# 目前进展
已测试：100个指定author的twitter爬取，几分钟可爬完1800-2000左右的tweets(每个author爬取最新20条tweets)，只用1个ip代理，加了fake agents，没被封- -

测试机器配置：
Mac OSX
CPU: 2.7 GHz Intel Core i5
Memory: 8 GB 1867 MHz DDR3

代理机器配置：
vultr虚拟机
CPU: 1vCore
RAM: 1024MB
OS: centOS7
