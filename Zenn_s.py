#
#
# # 1. read the folder , to output json file ,
#
#
#
import math

import requests
from lxml import etree




class CSBookOnePage(object):

    def __init__(self):
        pass


    def read_folder_output_template(self):

        """

        return:  1.urls_list , 2.output pro_template.html
        """
        # 1 读取文件目录，生成json格式的层级内容。同时剔除一些比如 .md 的内容，同时生成template
        # pro_template.html
        pass


    def pro_topContents_html(self):
        # 2 继承模板页面，生成项目目录contents的首页
        pass
        # 3 读取目录的文件内容，生成单页面的URL，请求后整理，并生成继承模板的单一文件的html文件。

    @staticmethod
    def read_folder(folderpath):
        pass

    def remove_get_rid_list(self,list_content):
        ret_list = []
        for item in list_content:
            for remove_item in get_rid_list:
                if remove_item in item:
                    ret_list.append(item)
                    # list_content.remove(item)
        [list_content.remove(x) for x in ret_list]
        return list_content

    def __recursive(self,url):
        ret = requests.get(url)
        element = etree.HTML(ret.text)

        article_nums = element.xpath('//*[@id="__next"]/header[2]/div/nav/a[1]/span/text()')
        article_title = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/h2/text()')
        article_urls = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/@href')
        f_article_urls = ["https://zenn.dev{0}".format(x) for x in article_urls]

        pages = math.ceil(float(int(article_nums[0])/48))

        for item in urls:

            if "tree" not in item:
                file_list.append("https://github.com{0}".format(item))
                print(item)
            elif "tree" in item and item not in folder_list:
                self.__recursive("https://github.com{0}".format(item))

    def last_name_htmlfile(self,url):
        # 借鉴其他的网站，只保留最后的文件即可
        htmlfile = url.split("/")[-1]+".html"

        return htmlfile



# ab -n 10000 -c 100  http://localhost:8080/

# 介绍python获取命令行参数的方法：getopt模和argparse模块。
import os
import sys
import getopt




import getopt
import sys


def main(argv):
    """

    python3 ab_test.py -r 10000 -c 10 -a http:127.0.0.1
    :param argv:
    :return:
    """
    topicurl =""

    try:
        options, args = getopt.getopt(argv, "ht:c:a:", ['help',"topic="])

        for option, value in options:
            if option in ("-t", "--topic"):
                topicurl  = value

        first_url = "https://zenn.dev/topics/{}?page=1".format(topicurl)

        ret = requests.get(first_url)
        element = etree.HTML(ret.text)

        article_nums = element.xpath('//*[@id="__next"]/header[2]/div/nav/a[1]/span/text()')
        article_title = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/h2/text()')
        article_urls = element.xpath('//*[@id="__next"]/div[1]/div/section/div[2]/div/div/article/div/a/@href')
        f_article_urls = ["https://zenn.dev{0}".format(x) for x in article_urls]

        pages = math.ceil(float(int(article_nums[0])/48))


        for i1,i2 in zip():
            


    except getopt.GetoptError:
        print("###################################################")
        print("\n")
        print("\n")
        print("\n")
        print("python3 run_rust.py -r test.rs")
        print("\n")
        print("\n")
        print("\n")
        print("###################################################")
        sys.exit()




if __name__ == '__main__':
    main(sys.argv[1:])


