
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

def exec(topicurl):
    first_url = "https://zenn.dev/topics/{0}?page=1".format(topicurl)

    ret = use_selenium_request(first_url)
    element = etree.HTML(ret)
    time.sleep(1)

    article_nums = element.xpath('//*[@id="__next"]/header[2]/div/nav/a[1]/span/text()')
    article_title = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/h2/text()')
    article_urls = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/@href')
    f_article_urls = ["https://zenn.dev{0}".format(x) for x in article_urls]

    for i1, i2 in zip(article_title, f_article_urls):
        one_str = str(i1 + " " + i2)
        writeintoTSV_file(topicurl + ".tsv", [one_str])

    f_nums = math.ceil(int(article_nums[0]) /48)

    for item in range(2,f_nums + 1):
        other_url = "https://zenn.dev/topics/{0}?page={1}".format(topicurl, str(item))
        ret = use_selenium_request(other_url)
        element = etree.HTML(ret)

        article_title = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/h2/text()')
        article_urls = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/@href')
        f_article_urls = ["https://zenn.dev{0}".format(x) for x in article_urls]

        for i1, i2 in zip(article_title, f_article_urls):
            one_str = str(i1 + " " + i2)
            writeintoTSV_file(topicurl + ".tsv", [one_str])

def main(argv):
    """

    python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1
    :param argv:
    :return:
    """
    topicurl = ""

    try:
        options, args = getopt.getopt(argv, "ht:c:a:", ['help', "topic="])

        for option, value in options:
            if option in ("-t", "--topic"):
                topicurl = value

        exec(topicurl)


    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 Zenn_s.py -t python")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(1)


    
