import unittest

from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler
from scrapy_redirect import RedirectMiddleware
from scrapy.http import Request, Response

class RedirectMiddlewareTest(unittest.TestCase):

    def setUp(self):
        self.crawler = get_crawler(Spider)
        self.spider = self.crawler._create_spider('foo')
        self.mw = RedirectMiddleware.from_crawler(self.crawler)

    def test_redirect(self):
        url = 'http://httpbin.org/status/301'

        req1 = Request(url)
        rsp1 = Response('http://httpbin.org/status/301', headers={'Location': '/redirect/1'}, status=301)
        req2 = self.mw.process_response(req1, rsp1, self.spider)
        rsp2 = Response('http:httpbin.org/redirect/1', headers={'Location': '/get'}, status=302)
        req3 = self.mw.process_response(req2, rsp2, self.spider) 

        self.assertEqual(req2.url, 'http://httpbin.org/redirect/1')
        self.assertEqual(req2.meta['redirect_urls'], ['http://httpbin.org/status/301'])
        self.assertEqual(req2.meta['redirect_times'], 1)
        self.assertEqual(req2.meta['redirect_status_code'], [301])
        self.assertEqual(req3.url, 'http://httpbin.org/get')
        self.assertEqual(req3.meta['redirect_urls'], ['http://httpbin.org/status/301','http://httpbin.org/redirect/1'])
        self.assertEqual(req3.meta['redirect_status_code'], [301, 302])