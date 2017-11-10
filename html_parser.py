# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, new_url, html_cont):
        if new_url is None or html_cont is None :
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')

        new_urls = self._get_new_urls(new_url,soup)
        new_data =  self._get_new_data(new_url,soup)

        return new_urls,new_data

    def _get_new_urls(self, new_url, soup):
        urls = set()
        # / item / % E7 % AE % 80 % E6 % B4 % 81
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links :
            url = link['href']
            new_full_url = urlparse.urljoin(new_url,url)
            urls.add(new_full_url)
        return urls


    def _get_new_data(self, new_url, soup):
        res_data = {}

        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        res_data['url'] = new_url

        return res_data