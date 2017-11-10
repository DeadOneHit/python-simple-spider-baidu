# coding:utf-8
from baikespider import html_download
from baikespider import html_parser
from baikespider import output_html
from baikespider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = output_html.HtmlOutput()



    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "current count : %d" % (count)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
            except:
                print "craw failed"
            if count ==20:
                break
            count = count+1
        self.output.output_html()


if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313'

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
