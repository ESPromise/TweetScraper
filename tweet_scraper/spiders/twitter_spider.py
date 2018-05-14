import scrapy
import logging
from tweet_scraper.items import TweetItem

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    #start_urls = ["https://www.twitter.com/realDonaldTrump"]
    start_authors = ['realDonaldTrump']
    
    def __init__(self):
        with open("authors") as f:
            for author in f:
                author = author.strip()
                self.start_authors.append(author)

    def start_requests(self):
        for author in self.start_authors:
            url = 'https://twitter.com/' + author
            yield scrapy.http.Request(url, meta={'author' : author}, callback=self.parse_page, dont_filter = True)

    def parse_page(self, response):
        item_selectors = response.css(".TweetTextSize")
        time_selectors = response.css("._timestamp")
        for item in self.parse_tweet_item(item_selectors, time_selectors, response.meta['author']):
            yield item

    def parse_tweet_item(self, item_selectors, time_selectors, author):
        if (len(item_selectors) != len(time_selectors)):
            logger.warning("wrong page") 
            return null

        for i in range(0, len(item_selectors)):
            tweet = TweetItem()
            #作者，由request直接传入
            tweet['author'] = author
           
            #发布时间
            times = time_selectors[i].xpath("./@data-time").extract()
            if (len(times) > 0):
                tweet['timestamp'] = times[0]

            #Tweets
            texts = item_selectors[i].xpath("./text()").extract()
            if (len(texts) > 0):
                tweet['text'] = texts[0]
            
            yield tweet

'''
    def parse(self, response):
        #authors = response.xpath('/html/body/main/div/div/div/div/div/blockquote/div/a/@href')
        authors = response.css(".TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text")

        item = Tweet()
        item['timestamp'] = 123;
        return item;

        with open("test_out", 'w') as f:
            for author in authors:
                tmp = author.extract()
                f.write(tmp + "\n")
'''
