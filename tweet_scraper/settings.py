# -*- coding: utf-8 -*-

# Scrapy settings for tweet_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tweet_scraper'

SPIDER_MODULES = ['tweet_scraper.spiders']
NEWSPIDER_MODULE = 'tweet_scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tweet_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

RANDOM_UA_PER_PROXY = True
FAKEUSERAGENT_FALLBACK = "Mozilla"

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#REDIRECT_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tweet_scraper.middlewares.TweetScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 100,
    'tweet_scraper.middlewares.MyproxiesSpiderMiddleware': 130,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
    #'scrapy_crawlera.CrawleraMiddleware': 600
} 

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tweet_scraper.pipelines.SaveToFilePipeline':100
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 10
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#settings for mongo db
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "twitter_data"             # database name to save the crawled data
MONGODB_TWEET_COLLECTION = "tweets"     # collection name to save tweets


#IP POOL
IPPOOL=[  
        {"ipaddr":"159.65.105.33:8888"},
        {"ipaddr":"34.238.142.123:8887"},
        {"ipaddr":"104.129.180.63:8887"},
        {"ipaddr":"13.113.17.173:8887"},
        {"ipaddr":"138.128.218.91:8887"},
]  
#IPPOOL=[
#    {"ipaddr":"127.0.0.1:8118"}
#]

#authors
AUTHORS=[     
    "VitalikButerin",
    "SatoshiLite",
    "brian_armstrong",
    "rogerkver",
    "aantonop",
    "NickSzabo4",
    "dtapscott",
    "gavinandresen",
    "com/jihanwu",
    "laurashin",
    "thomaspower",
    "ErikVoorhees",
    "tylerwinklevoss",
    "barrysilbert",
    "TuurDemeester",
    "VinnyLingham",
    "CharlieShrem",
    "petertoddbtc",
    "adam3us",
    "ToneVays",
    "lopp",
    "TimDraper",
    "jgarzik",
    "bobbyclee",
    "fredwilson",
    "naval",
    "arrington",
    "jonmatonis",
    "StephanTual",
    "jimmysong",
    "cburniske",
    "DerinCag/",
    "FEhrsam",
    "VentureCoinist",
    "dinisguarda",
    "michaelkitces",
    "CarpeNoctom",
    "ethereumjoseph",
    "AriDavidPaul",
    "twobitidiot",
    "josephzhou",
    "brockpierce",
    "CremeDeLaCrypto",
    "novogratz",
    "dahongfei",
    "woonomic",
    "gavofyork",
    "niccary",
    "eric_lombrozo",
    "VladZamfir",
    "bgarlinghouse",
    "starkness",
    "iam_preethi",
    "kyletorpey",
    "IOHK_charles",
    "leashless",
    "com/Melt_Dem",
    "desantis",
    "slushcz",
    "bitcoinbyte",
    "SunnyStartups",
    "anondran",
    "alextapscott",
    "wmougayar",
    "proffaustus",
    "ryanxcharles",
    "Kris_HK",
    "ummjackson",
    "MrChrisEllis",
    "alansilbert",
    "dan_pantera",
    "muneeb",
    "nejc_kodric",
    "mbauwens",
    "francispouliot_",
    "OneMorePeter",
    "oleganza",
    "eiaine",
    "cryptomanran",
    "com/SusanneChishti",
    "_jonasschnelli_",
    "pierre_rochard",
    "ljxie",
    "juanbenet",
    "chrislarsensf",
    "spair",
    "iamjosephyoung",
    "prestonjbyrne",
    "bendavenport/",
    "AriannaSimpson",
    "HeyTaiZen",
    "alexsunnarborg",
    "TonyGallippi",
    "AnselLindner",
    "dieguito",
    "certainassets",
    "joonian",
    "roasbeef",
    "oscarwgrut",
    "derose",
]

