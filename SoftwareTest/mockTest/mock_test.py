# coding=utf-8
from mock import MagicMock
from mock import Mock

obj = MagicMock()
print dir(obj)
# ['assert_any_call', 'assert_called', 'assert_called_once', 'assert_called_once_with', 'assert_called_with', 'assert_has_calls', 'assert_not_called', 'attach_mock', 'call_args', 'call_args_list', 'call_count', 'called', 'configure_mock', 'method_calls', 'mock_add_spec', 'mock_calls', 'reset_mock', 'return_value', 'side_effect']

# name参数
mockObj = Mock(name='foo')
print mockObj  # <Mock name='foo' id='97011504'>
print repr(mockObj)  # <Mock name='foo' id='97011504'>

# return_value参数
# a.指定的是某个值
mockFoo = Mock(return_value=100)
print mockFoo  # <Mock id='94471824'>
mockObj = mockFoo()
print mockObj  # 100

# b.指定的是某个类的对象
class Foo(object):
    _num = 100

    def fun1(self):
        print 'call fun1'

    def fun2(self, argValue):
        print 'value = ', argValue


fooObj = Foo()
print fooObj  # <__main__.Foo object at 0x05C84690>
mockFoo = Mock(return_value=fooObj)
print mockFoo  # <Mock id='97010928'>
mockObj = mockFoo()
print mockObj   # <__main__.Foo object at 0x05D30730>
print mockObj._num  # 100
print mockObj.fun1()
# call fun1
# None
print mockObj.fun2(99)
# value =  99
# None

# side_effect参数
# a.指定的参数的值是异常
# mockFoo = Mock(return_value=100, side_effect=StandardError)
# print mockFoo()
# Traceback (most recent call last):
#   File "E:/core/python/softwareTest/mockTest/mock_test.py", line 43, in <module>
#     print mockFoo()
#   File "C:\Python27\lib\site-packages\mock\mock.py", line 1062, in __call__
#     return _mock_self._mock_call(*args, **kwargs)
#   File "C:\Python27\lib\site-packages\mock\mock.py", line 1118, in _mock_call
#     raise effect
# StandardError
# 当side_effecr被设置的时候，return_value就被屏蔽了，不起作用了，上边side_effect被设置的是一个异常。

# b.指定的参数的值是一个list或者tuple
fooList = [100, 200, 300]
mockFoo = Mock(return_value=50, side_effect=fooList)
mockObj = mockFoo()
print mockObj   # 100
print mockObj   # 100
mockObj = mockFoo()
print mockObj   # 200

# spec 参数
# a.指定的是属性组成的list
specList = ["_value","callFun1"]
mockFoo = Mock(spec=specList)
print mockFoo   # <Mock id='101022608'>
print mockFoo._value    # <Mock name='mock._value' id='101023408'>
print mockFoo.callFun1  # <Mock name='mock.callFun1' id='101020752'>

# b.指定的是一个类的属性
mockFoo = Mock(spec=Foo)
print mockFoo   # <Mock spec='Foo' id='91130384'>
print mockFoo._num  # <Mock name='mock._num' id='91129008'>
print mockFoo.fun1()    # <Mock name='mock.fun1()' id='91130512'>
# spec设置的是mock对象的属性，所以，这下，mock就有了3个属性了。


