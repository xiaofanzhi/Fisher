



# 线程隔离werkzeug local Local 字典


# L 线程隔离对象
import threading
import time
from werkzeug.local import Local,LocalStack


# class A:
#     b = 1
#
# m = Local()
# m.b = 1
# def worker():
#     m.b =100
#     print('new',m.b)
#
# new = threading.Thread(target=worker,name='qq')
# new.start()
# time.sleep(1)
#
# print(m.b)


s=LocalStack()
s.push(1)
print(s.top)
print(s.top)