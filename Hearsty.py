import urllib, httplib2, os, sys, csv, time
from httplib import BadStatusLine
try:
	import json
except ImportError:
	import simplejson as json

####SETTINGS####
hearst_api_key = ''
hearst_url_base = 'http://hearst.api.mashery.com/'

http = httplib2.Http()

def postToCloudmine():
	data = "{\"data\":\"21\"}";
	url = '/' + cloudmine_app + '/text'
	headers = {'Content-type': 'application/json', 'X-CloudMine-ApiKey':cloudmine_api_key}
	response, content = http.request(cloudmine_url_base+url, 'POST', headers=headers, body=data)
	print str(response) + '\t' + str(content)

def ArticleSearch(keywords, limit, hearst_api_key):
	# http://hearst.api.mashery.com/Article/search?_pretty=1&shape=brief&start=0&limit=10&sort=publish_date%2Cdesc&total=0&api_key=
	if limit == '':
		limit = 10;
	call_type = 'Article'
	url = '/' + call_type + '/search?_pretty=1&shape=brief&start=0&limit=' + str(limit) + '&sort=publish_date%2Cdesc&total=0&api_key='+hearst_api_key
	if keywords != '':
		url += '&keywords=' + keywords
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def ArticleImageSearch(caption, description, keywords, limit, hearst_api_key):
	# http://hearst.api.mashery.com/ArticleImage/search?_pretty=1&shape=brief&start=0&limit=10&sort=name%2Casc&total=0&api_key=
	call_type = 'ArticleImage'
	if limit == '':
		limit = 10;
	url = '/' + call_type + '/search?&_pretty=1&shape=full&start=0&limit=' + str(limit) + '&sort=name%2Casc&total=0'
	if caption != '':
		url += '&caption=' + caption
	if description != '':
		url += '&description=' + description
	if keywords != '':
		url += '&keywords=' + keywords
	url += '&api_key='+hearst_api_key
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def ArticleSectionSearch(keywords, limit, hearst_api_key):
	# http://hearst.api.mashery.com/ArticleSection/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
	call_type = 'ArticleSection'
	if limit == '':
		limit = 10;
	url = '/' + call_type + '/search?_pretty=1&start=0&limit=' + str(limit) + '&sort=name%2Casc&total=0&api_key='+hearst_api_key
	if keywords != '':
		url += '&keywords='+keywords
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def AuthorSearch(limit, first_name, last_name, hearst_api_key):
	# http://hearst.api.mashery.com/Author/search?_pretty=1&start=0&limit=10&sort=last_name%2Casc&total=0&api_key='+hearst_api_key
	call_type = 'Author'
	if limit == '':
		limit = 10;
	url = '/' + call_type + '/search?_pretty=1&start=0&limit=' + str(limit) + '&sort=last_name%2Casc&total=0&api_key='+hearst_api_key
	if first_name != '':
		url += '&first_name='+first_name
	if last_name != '':
		url += '&last_name='+last_name
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def ArticleTypeSearch(limit):
	# http://hearst.api.mashery.com/ArticleType/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
	if limit == '':
		limit = 10;
	call_type = 'ArticleType'
	url = '/' + call_type + '/search?_pretty=1&start=0&limit=' + str(limit) + '&sort=name%2Casc&total=0&api_key='+hearst_api_key
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def SourceSearch(name, limit):
	# http://hearst.api.mashery.com/Source/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
	if limit == '':
		limit = 10;
	call_type = 'Source'
	url = '/' + call_type + '/search?_pretty=1&start=0&limit=' + str(limit) + '&sort=name%2Casc&total=0&api_key='+hearst_api_key
	if name != '':
		url += '&name=' + name
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def AdCategorySearch():
	# http://hearst.api.mashery.com/AdCategory/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
 	call_type = 'AdCategory'
	url = '/' + call_type + '/search?_pretty=1&start=0&limit=100&sort=name%2Casc&total=0&api_key='+hearst_api_key
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)
	
def ArticleCategorySearch():
	http://hearst.api.mashery.com/ArticleCategory/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
	call_type = 'ArticleCategory'
	url = '/' + call_type + '/search?'
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)
	
def TemplateSearch():
	http://hearst.api.mashery.com/Template/search?_pretty=1&start=0&limit=10&sort=name%2Casc&total=0&api_key='+hearst_api_key
	call_type = 'Template'
	url = '/' + call_type + '/search?'
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)

def SiteSearch():
	http://hearst.api.mashery.com/Site/search?_pretty=1&start=0&limit=10&sort=site_name%2Casc&api_key=8qgkp2gtvrbudmfq2mvc2qrv
	call_type = 'Site'
	url = '/' + call_type + '/search?'
	headers = {}
	body = {}
	response, content = http.request(hearst_url_base+url, 'GET', headers=headers, body=body)
	print str(response) + '\t' + str(content)
