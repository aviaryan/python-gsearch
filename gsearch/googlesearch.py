# -*- coding: utf-8 -*-

from __future__ import print_function

import re
import traceback
import sys
from random import choice

try:
	# Python 3
	from urllib import request
	from html.parser import HTMLParser # keep it to avoid warning
	from html import unescape
	from urllib.parse import quote
	# local
	try:
		from gsearch.data import user_agents
	except ImportError:
		from data import user_agents
except ImportError:
	# Python 2
	import urllib2 as request
	from urllib import quote
	from HTMLParser import HTMLParser
	# local
	from data import user_agents

# placeholder
isPython2 = sys.version.startswith('2')


def download(query, num_results):
	"""
	downloads HTML after google search
	"""
	# https://stackoverflow.com/questions/11818362/how-to-deal-with-unicode-string-in-url-in-python3
	name = quote(query)

	name  = name.replace(' ','+')
	url = 'http://www.google.com/search?q=' + name
	if num_results != 10:
		url += '&num=' + str(num_results)  # adding this param might hint Google towards a bot
	req = request.Request(url, headers={
		'User-Agent' : choice(user_agents),
		# 'Referer': 'google.com'
	})
	try:
		response = request.urlopen(req)
	except Exception:  # catch connection issues
		# may also catch 503 rate limit exceed
		print('ERROR\n')
		traceback.print_exc()
		return ''
	# response.read is bytes in Py 3
	if isPython2:
		# trick: decode unicode as early as possible
		data = response.read().decode('utf8', errors='ignore')
	else:
		data = str(response.read(), 'utf-8', errors='ignore')
	# print(data)
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
	if isPython2:
		h = HTMLParser()
		s = h.unescape(text)
	else:
		s = unescape(text)
	return s


def search(query, num_results=10):
	"""
	searches google for :query and returns a list of tuples
	of the format (name, url)
	"""
	data = download(query, num_results)
	results = re.findall(r'\<h3.*?\>.*?\<\/h3\>', data, re.IGNORECASE)
	if results is None or len(results) == 0:
		print('No results where found? Did the rate limit exceed?')
		return []
	# search has results
	links = []
	for r in results:
		mtch = re.match(r'.*?a\s*?href=\"(.*?)\".*?\>(.*?)\<\/a\>.*$', r, flags=re.IGNORECASE)
		if mtch is None:
			continue
		# parse url
		url = mtch.group(1)
		# clean url https://github.com/aviaryan/pythons/blob/master/Others/GoogleSearchLinks.py
		url = re.sub(r'^.*?=', '', url, count=1) # prefixed over urls \url=q?
		url = re.sub(r'\&amp.*$', '', url, count=1) # suffixed google things
		# url = re.sub(r'\%.*$', '', url) # NOT SAFE, causes issues with Youtube watch url
		# parse name
		name = prune_html(mtch.group(2))
		name = convert_unicode(name)
		# append to links
		if is_url(url): # can be google images result
			links.append((name, url))
	return links


def run():
	"""
	CLI endpoint to run the program
	"""
	if len(sys.argv) > 1:
		print(search(sys.argv[1]))
	else:
		# print(search('Kimi no na wa'))
		print(search('君の名'))


if __name__ == '__main__':
	run()
