from redis import Redis

cache = Redis(host='192.168.0.6', port=6379, password='root')

for x in range(3):
    cache.publish('email', "xxx.qq.com")