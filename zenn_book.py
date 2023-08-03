
import sys



import csv
import math
import math

import requests
from lxml import etree
# ab -n 10000 -c 100  http://localhost:8080/

# 介绍python获取命令行参数的方法：getopt模和argparse模块。
import os
import sys
import getopt

import getopt
import sys


import time
from requests.exceptions import ConnectionError
from selenium import webdriver
from lxml import etree
import datetime
driver = webdriver.Chrome()



import os
import requests
import urllib.request

from retrying import retry
from urllib.error import URLError
import os



def retry_if_io_error(exception):
    return isinstance(exception,URLError)

#  重复请求

class DownloadIMG():

    @retry(retry_on_exception=retry_if_io_error)
    def exec(self,url,filename):
        imgName = self.make_filename(filename)
        self.download_image(url,imgName)
        print("{0} :  ----  OK  ---- ".format(filename))


    # 画像をダウンロードする
    def download_image(self,url,imgPath):
        urllib.request.urlretrieve(url,imgPath)

    # 画像のファイル名を決める
    def make_filename(self,filename):
        image_path = os.path.join(os.getcwd(),"images")
        if bool(os.path.exists(image_path)) != True:
            os.mkdir("images")

        imgName = filename + ".png"
        fullpath = os.path.join(image_path, imgName)
        return fullpath



def writeintoTSV_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
def use_selenium_request(url):

    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    # time.sleep(3)
    return html








def exec():
    for item in range(1,25):

        first_url = "https://zenn.dev/books?order=latest&page={0}".format(str(item))

        ret = use_selenium_request(first_url)
        element = etree.HTML(ret)
        time.sleep(1)

        article_image = element.xpath('//*[@id="__next"]/section/div[1]/div/div/article/a[1]/div/div[1]/img/@src')
        article_title = element.xpath('//*[@id="__next"]/section/div[1]/div/div/article/a[1]/h3/text()')
        article_price = element.xpath('//*[@id="__next"]/section/div[1]/div/div/article/a[1]/div/div[2]/text()')
        article_urls = element.xpath('//*[@id="__next"]/section/div[1]/div/div/article/a[1]/@href')
        f_article_urls = ["https://zenn.dev{0}".format(x) for x in article_urls]

        for i1, i2,i3,price in zip(article_title, f_article_urls,article_image,article_price):
            if price == "0":

                one_str = str(i1 + " " + i2)
                writeintoTSV_file("zenn_book.tsv", [one_str])
                i1 = i1.replace("/","")
                i1 = i1.replace("'","")
                i1 = i1.replace('"',"")
                i1 = i1.replace('!',"")
                try:


                    instanceDownloadIMG.exec(i3,i1)
                    # time.sleep(0.1)
                except BaseException as e:
                    print(e)






if __name__ == '__main__':
    instanceDownloadIMG = DownloadIMG()
    exec()


