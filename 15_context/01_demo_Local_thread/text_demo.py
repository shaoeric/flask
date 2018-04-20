from threading import Thread

# request = '123'
# class MyThread(Thread):
#     def run(self):
#         global request
#         request = 'abc'
#         print("子线程", request)
#
# mythread = MyThread()
# mythread.start()
# mythread.join()  # 子线程运行完毕 才继续运行下面的代码
# print("主线程", request)
# >>子线程 abc
# 主线程 abc

from werkzeug.local import Local  # 再导入Local
local = Local()
local.request = '123'

class MyThread(Thread):
    def run(self):
        local.request = 'abc'
        print("子线程", local.request)
mythread = MyThread()
mythread.start()
mythread.join()
print("主线程", local.request)