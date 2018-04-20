from redis import Redis

cache = Redis(host='192.168.0.6', port=6379, password='root')

# 1.操作字符串
# cache.set('username', 'eric', ex=20)
# print(cache.get('username'))
# cache.delete('username')

#  2.列表操作
# cache.lpush('languages', 'java')
# cache.lpush('languages', 'python')
# cache.rpush('languages', 'php')
# print(cache.lrange('languages', 0, -1))

# # 3.集合操作
# cache.sadd('team', 'li')
# cache.sadd('team', 'huang')
# cache.sadd('team', 'zhang')
# print(cache.smembers('team'))

# 4.哈希操作
# cache.hset('website', 'baidu', 'www.baidu.com')
# cache.hset('website', 'google', 'www.google.com')
# print(cache.hgetall('website'))

# 5.事务操作
# pip = cache.pipeline()
# pip.set('username', 'eric')
# pip.set('password', '1111')
# pip.execute()

# 6.发布与订阅
#   异步发送邮件功能
ps = cache.pubsub()
ps.subscribe('email')
# 监听email频道，，发布在publish_email中
while True:
    for item in ps.listen():
        print(item)
