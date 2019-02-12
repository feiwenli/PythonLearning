# coding = -utf-8
import functools
import time
from inspect import isfunction

'''既支持@log，又支持@log('parameter')'''


# 法1
def log(fn):
    if not isfunction(fn):
        # 有参
        def decorator(func):
            # 用来把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin:')
                print('%s %s():' % (fn, func.__name__))
                f = func(*args, **kw)
                print('end:')
                return f

            return wrapper

        return decorator
    else:
        # 无参
        @functools.wraps(fn)
        # 用来把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
        def wrapper(*args, **kw):
            print('call %s():' % fn.__name__)
            # func(*args,**kw)
            return fn(*args, **kw)  # 感觉没差

        return wrapper


# 法2
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('Begin call')
            text_ = text
            if isfunction(text_):
                # 无参默认值
                text_ = 'call'
            print('%s %s():' % (text_, func.__name__))
            f = func(*args, **kw)
            print('End call')
            return f

        return wrapper

    return decorator(text) if isfunction(text) else decorator


@log('execute')  # 相当于now = log('execute')(now)
def now():
    print('2017-8-23')


@log
def today():
    print(time.asctime(time.localtime(time.time())))


# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
print(now.__name__)
now()
today()
