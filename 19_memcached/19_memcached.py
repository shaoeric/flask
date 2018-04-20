import memcache

# 连接之前 要先确保启动memcached
mc = memcache.Client(["127.0.0.1:11211"], debug=True)
# 为达到分布式,ip地址端口号 写成字典形式["127.0.0.1:11211", "192.168.0.102:11211"]

mc.set('username', 'eric', time=120)
# mc.set_multi({'title':'钢铁', 'content': 'hello'}, time=120)
username = mc.get('username')
print(username)
mc.delete('username')
username = mc.get('username')
print(username)
