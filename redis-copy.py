# -*- coding:utf-8 -*-

import redis
import re

source = redis.Redis(host="localhost", port=1221,password=None,socket_timeout=None,
	connection_pool=None, charset='utf-8', errors='strict', decode_responses=False, unix_socket_path=None)

target = redis.Redis(host="localhost", port=2222,password=None,socket_timeout=None,
	connection_pool=None, charset='utf-8', errors='strict', decode_responses=False, unix_socket_path=None)

component = re.compile('component:\d+')
component_path = re.compile('component-path*')
component_category = re.compile('component:category*')

for key in source.keys(pattern="*"):
	if component.search(key):
		content = source.hgetall(key)
		target.hmset(key,content)
	if component_path.search(key):
		content = source.get(key)
		target.set(key,content)
	if component_category.search(key):
		ids = source.smembers(key)
		pipe = target.pipeline()
		for id in ids:
			pipe.sadd(key,id)
		pipe.execute()

print "Done"


			

		




