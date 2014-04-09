# coding:utf-8

import redis

r = redis.Redis(host="localhost", port="2222",password=None)

pipe = r.pipeline()

for key in r.keys(pattern="*"):
	pipe.delete(key)

pipe.execute()

print "Done"
	


