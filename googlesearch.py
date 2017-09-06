# -*- coding: utf-8 -*-

from __future__ import print_function

import re

try:
	# Python 3
	from urllib import request
	from html.parser import HTMLParser
except ImportError:
	# Python 2
	import urllib2 as request
	from HTMLParser import HTMLParser


def download(query, num_results=15):
	"""
	downloads HTML after google search
	"""
	name = query
	name  = name.replace(' ','+')
	url = 'http://www.google.com/search?q=' + name + '&num=' + str(num_results)
	req = request.Request(url, headers={'User-Agent' : "foobar"})
	response = request.urlopen(req)
	data = response.read()
	return data


def is_url(url):
	"""
	checks if :url is a url
	"""
	regex = r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'
	return re.match(regex, url) is not None


def prune_html(text):
	"""
	https://stackoverflow.com/a/42461722/2295672
	"""
	text = re.sub(r'<.*?>', '', text)
	return text


def convert_unicode(text):
	"""
	converts unicode HTML to real Unicode
	"""
	h = HTMLParser()
	s = h.unescape(text)
	return s


def search(query, num_results=15):
	"""
	searches google for :query and returns a list of tuples
	of the format (name, url)
	"""
	data = download(query, num_results)
	if type(data) != str: # in Python 3
		data = str(data, 'utf-8', errors='ignore')
	results = re.findall(r'\<h3.*?\>.*?\<\/h3\>', data, re.IGNORECASE)
	if results is None:
		return []
	# search has results
	links = []
	for r in results:
		mtch = re.match(r'.*?a\s*?href=\"(.*?)\"\s*?\>(.*?)\<\/a\>.*$', r, flags=re.IGNORECASE)
		if mtch is None:
			continue
		# parse url
		url = mtch.group(1)
		# clean url https://github.com/aviaryan/pythons/blob/master/Others/GoogleSearchLinks.py
		url = re.sub(r'^.*?=', '', url, count=1) # prefixed over urls \url=q?
		url = re.sub(r'\&amp.*$', '', url, count=1) # suffixed google things
		url = re.sub(r'\%.*$', '', url) # NOT SAFE
		# parse name
		name = prune_html(mtch.group(2))
		name = convert_unicode(name)
		# append to links
		if is_url(url): # can be google images result
			links.append((name, url))
	return links


if __name__ == '__main__':
	print(search('Avi Aryan'))
