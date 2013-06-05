#!/usr/bin/python
# coding:utf-8
# Copyright 2013--2015.
# Licensed under the Apache License, Version 1
# http://www.apache.org/licenses/LICENSE-2.0

# Word_Searching Script
# Author: fish
# Email: fsh267@gmail.com
# http://www.love67.net
# usage1: 'python **.py word' to find the word's explination or
# usage2: 'python **.py word -detail' to list the phrase of the word
from bs4 import BeautifulSoup
import sys
import urllib2


def input_error():
    print "usage1: 'python **.py word' or "
    print "usage2: 'python **.py word -detail"


def main():
    length = len(sys.argv)
    # 读入命令行
    if length < 2:
        input_error()
        sys.exit()
    else:
        word = sys.argv[1]
        # url是有道翻译的对应网页
    url = 'http://dict.youdao.com/search?le=en&q=%s&keyfrom=dict.index' %word
    # urlopen函数调用
    #print url
    data = urllib2.urlopen(url).read()
    #print data
    # 将data网页源代码放到soup中，便于匹配
    soup = BeautifulSoup(data)
    # soup.find() 可以放入标签和class名称
    word_div = soup.find('div', 'trans-container')
    if not word_div:
    	print 'word does not exists'
    	sys.exit()
    # word_div存了一个标签，每个单词意思，存在每个<li>**</li>中,格式化输出，不带'<li></li>'
    for word_explination in word_div.find_all('li'):
        print str(word_explination)[4: -5]

    #第二种输入，还得显示出单词组成的短语
    #BeautifulSoup提供的find函数可以查找'p', 'a','span'等html标志语言模块
    if length == 3:
        if sys.argv[2] != '-detail':
            input_error()
        else:
        	raw_explination = ''
        	span = soup.find_all('p', 'wordGroup')
        	#最后一组词组有问题，删去了
        	for element in span[ : -1]:
        		link = element.find('a')

        		#转化成字符串，用于定位到解释那里
        		raw_explination += str(element)
        		location 	= raw_explination.find('</span>')
        		#格式化单词解释，</span>长度为7, </p>长度为4, 只采用第一个意思
        		explination = raw_explination[location + 7 : -4].split()[0]
        		#python 自带的输出对齐, ljust(num), rjust(num)
        		print link.string.ljust(25), explination
        		raw_explination = ''

if __name__ == '__main__':
	main()