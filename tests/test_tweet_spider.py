import pytest
import sys

sys.path.append("..")

from tweet_scraper.spiders.twitter_spider import TwitterSpider

class TestTwitterSpider:
    def test_parse_page(self):
        assert True
