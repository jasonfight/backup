笔记-12.05:
闭包(函数的嵌套):
1.类的定义
   定义:面向对象程序设计中,类是一种面向对象计算机编程语言的构造,是创建对象的模板,描述了所常见的对象共同的属性和方法
    类的数据:长远变量或者实例变量
    类的方法:即成员方法,简称方法,是操作数据的飞马,用于定义如何使用成员变量,因此一个类的行为和接口都是通过方法定义的.
    方法和变量:
    私有:内部使用
    公共:外部可见
2 类的创建:
__metaclass__ = type
class Person(object):
    age = 10
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
    def color(self,color):
        print '%s is %s'%(self.name,color)
1) __metaclass__ = type
    表示创建的类使用新式类,可以默认不加
2) class Person (object):
     定义了一个名为Person的类,类的名称一般用大写字母开头,object 为继承的父类
3) age=10
    成员变量,属于这个类的属性,即通过这个类创造的对象狗会有这个属性
4) def __init__(self.name):
    初始化方法,也称为构造函数,不写时,,系统会自动添加一个空的初始化函数,写了,就会发费原有的
,同时,需要在实例化一个对象时,需要传递相应的参数给这个初始化函数
5)def getName(self): 和 def color(self,color):
    成员方法,也是类的属性,即这个类实例化的对象会拥有这些方法,这些方法和普通的函数不同,
    在第一个参数都有一个"self"参数,这个是语法需要,在传参数不会给这个参数传参,而是在调用时,会自动的
把调用对象传递给这个参数

3.类的实例化;

    类提供默认行为,是实例的工厂,类中的行为是通过实例调用类完成的,在python中比较特殊的是,在类之外
可以通过实例对象直接为这个对象增添属性,除了我们定义的属性变量和方法外,类的实例本身还会有一些系统属性

lilei = Person('lilei')
即实例化了一个对象lilei,后面括号中了'lilei'作为参数,传递到__init__ 方法中.

__new__ 构造器

__del__  解构器

静态方法和类方法:
class class

继承:
继承描述了基类的属性如何传递给派生类,一个子类可以继承她的基类的任何属性,不管数据属性还是方法,

继承是面向对象编程中的一个重要概念,如果类A继承于类B,则成为A是B的子类,B为A的父类或者基类,
object 类是python中所有类的基类,及不谢继承关系时,需要写 object

继承的优点:
1.可以实现代码重用,
2.实现属性和方法继承
3.一个类在继承父类的同事也拥有自己特有的方法和属性,当父类重名的时候,会覆盖父类的方法属性

多重继承:

Python支持多重继承,只需要在括号内将多个继承的类用逗号隔开就行,
语法:
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass
此时 C 同时继承A和B的属性和方法

继承顺序,则可以通过mro函数来计算

继承检测:
用来检测一个类是否继承与另一个类:
语法:  issubclass(A,B)  检测A是否继承于B  返回值为True或这False

format 函数
str.format(*args,**kwargs)->string
eg:  s='{} is {}'.format(1,2)------>  s='1 is 2'

super 函数:
    初始化函数的继承跟一般方法的继承有些不同,在子类中无法直接使用父类的初始化函数
此时,需要借助 super 函数来调用父类的方法
语法: super (当前子类名字,self . 父类的方法)

封装:
    面向对象的三个重要特征之一,封装是对对象的一种抽象,即将某些部分隐藏起来,对程序或者模块外部不可见
无法调用,封装离不开私有化,几将类或者函数中的某些属性限制在某个区域之内,外部无法调用,python中比较简单,
在准备私有话的属性名字前假双下划线就好.
class Protect(object):
    def __init__(self):
        self.job = "teacher"
        self.__name = "jason"
    def __python(self):
        print 'nihoa python'
    def code(self):
        print 'code....'
        self.__python()

if __name__ == '__main__':
    p = Protect()
    print p.job
    print p.__name
    p.code()
    p.__python()

def __init__(self):
    self.job = "teacher"
    self.__name = "jason"
初始化函数,self.job 和 self.__name两个属性,其中,self.job为一般属性
self.__name为私有化属性

def __python(self):
        print 'nihoa python'
声明一个__python的方法,为一个私有方法,实例化的时候不能直接调用

def code(self):
    print 'code....'
    self.__python()
声明一个普通方法code,里面有一个print语句和一个调用私有化属性的一个语句

if __name__ == '__main__':

测试时使用,在直接执行该模块是,模块的__name__值为__main__
在调用该模块是,模块的__name__ 为该模块的名称,所以,在测试时直接运行该模块
if语句成立,执行if内的语句.
p = Protect()       # NOTE: 实例化一个对象p
print p.job     # NOTE: 输出 'teacher'
print p.__name  # NOTE: 私有化的属性,不能直接调用,无法执行
p.code()       # NOTE: 调用code方法,执行code中的语句,此时,code中的self.__python()可以被执行
p.__python()   # NOTE: 直接调用__python方法,不能被调用,无法执行

多态:
多态是面向对象程序执行是,相同的信息可能会送给多个不同的类别对象,系统可根据对象所数类别
不同,引发对应类别的方法,而同时又采取不同的行为,简单来说就是,给予不同的对象引发不同的动作
eg:
'This is a book'.count('s')   输出: 2
[1,2,3,3,3,3].count(3)  输出 4


魔法方法 属性和迭代器

在python中,有的方法和属性名称前后都会有两个下划线,这种方法或者属性成为魔法方法(属性)
一般这种方法由系统定义,有特殊的含义,可一通过dir()函数进行查看一个对象有什么魔法方法(属性)
比较常用的魔法方法:
1.常用的几个魔法方法一
class A(object):
    '''magic'''         # NOTE: 编辑A的帮助文档
    pass
a=A()
print a.__doc__     # NOTE: 输出 magic   A的帮助文档
print a.__class__ # NOTE:  输出<class '__main__.A'> 类名
print a.__dict__    # NOTE: 输出{}  一个空字典
2.常用的几个魔法方法二
class A(object):
    pass
a=A()
a.x
此时,a.x语句显然会报错,因为A没有名称为x的属性,如果想先定义一个变量,在后面的某个特定的位置传参时
需要使用特殊方法进行拦截
class A(object):
    def __getattr__(self,name):
        print 'getattr....'
    def __setattr__(self,name,value):
        self.__dict__[name] = value

    pass
a = A()
a.x         # NOTE: 调用getattr方法
a.x = 7     # NOTE: 调用setattr方法
print a.x

getattr(self,name)如果name被访问,自动调用该方法
setattr(self,name,value):如果要给name赋值,自动调用该方法

迭代器和生成器:
迭代器:
迭代算法是计算机解决问题的一种基本算法,它利用计算机运算速度块,适合做
重复性操作的特点,给计算机一组指令(或一定的步骤)进行重复执行,在每次执行
时,都从变量的原值推出一个它的新值,列表,元组,字典,文件都可以用iter的方法
生成迭代对象,然后用next方法,进行访问,

class TestIter(object):
    def __init__(self,a):
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 1
        return self.a ** 2

a = TestIter(2)
print a.__next__()  # NOTE: 输出 9

迭代器不能后退,只能向前,另外迭代器也不适合在多线程环境中对可便集合使用

生成器:

生成器是一次成成一个值的特殊类型函数,可以将其视为可恢复函数,调用该函数将返回
一个可用于生成连续x值的生成器,简单的说局势在函数执行过程中,yield 语句会把需要的值
返回给调用的函数,然后记录下位置,继续执行,而生成器内的所有变量参数都会被保存下来供下一次
使用

def fib(max):
    a,b = 1,2
    while a < max:
        yield a
        a,b=b,a+b

for i in fib(20):
    print i
# NOTE: 每当yield一个a 执行一次for语句,即如果a返回5个,则该for语句打印5次

错误与异常:

错误:人为的一些错误,即语法使用不当,拼写错误,或是逻辑上不合法等,会导致程序不能白解释器解释
或被编译器编译,错误必须在程序执行前纠正,一般如果程序出现错误,编译器就会给出预定的提示,程序员
可以通过提示来分析修改错误

异常:异常是因为程序出现了错误而在正常控制利用以外采取的行为,分为两个阶段,首先是引起异常发生的错误,
然后是检测(并餐区某些措施)阶段,异常是程序运行时发生的错误,主要是由外部原因引起的,不是简单的语法错误,
这些因素不在程序员的直接控制下,比如,坟墓分母为0 这种情况.

异常处理:
常见的异常:
Exception:所有异常的基类,python中所有的异常都是基类 Exception 中的一员,
异常都是从基类 Exception 中继承,并在该模块中定义的
AttributeError 属性错误,特性引用和赋值失败时会引发该错误
NameError:试图访问的变量名不存在
SyntaxError:语法错误
KeyError:使用了不存在的键
IndexError:索引错误,索引不存在或者超出范围
TypeError:类型错误,
ZeroDivisionError:除数为0错误
ValueError:值错误,传给对象的参数类型不正确,比如给int()中传入字符串

try...except...语句

    如果没有出现错误,则跳过 except 语句,正常执行程序,如果 try 语句中出现错误,错误语句
后面的语句会被忽略,直接调到 except 语句来捕获错误类型,根据错误类型执行相关操作,

处理多个异常:
    捕获到不同的异常采取不同的语句块来进行处理,一个 except 语句 可以跟 多个错误类型,
中间使用逗号隔开,即可将这几种错误类型,都采取同一处理手段
finally 和 else 语句
else 语句:
    执行完 try 语句后会执行 else 语句,每当程序出现异常,即执行了 except 语句时,else 的
语句就不会执行了,即 try 语句中没有错误时,会执行 else 语句
finally 语句:
    无论语句是否有异常,都执行finally语句

def A(x):
    try:
        a = 3 / x
        print a
    except (ZeroDivisionError,ValueError):
        print '0!'
    except TypeError:
        print 'str'
    else :
        print "else..."
    finally:
        print 'finally.....'
A(0)        # NOTE: 输出 0!  finally...
A('123')    # NOTE: 输出 str finally...
A(1)        # NOTE: 输出 3   slse... finally...

输出错误的所在行及信息:

1.现在模块中引入 traceback 模块
    语法: import traceback
2.在except 语句块中添加traceback方法:
    语法: traceback.print_exc()

显式触发异常  raise 语句
    raise 用于显式触发异常,一般形式很简单,在 raise 后跟一个类或者类的实例就可以
如果自己创建一个类,则这个类需要继承于 Exception

class MyError(Exception): # NOTE:  自定义一个错误类型
    pass
try:
    s = None
    if s is None:
        print 'A'
        raise MyError('B')  # NOTE:  符合条件时,执行 raise 语句,括号中写弹出内容
except MyError as x:        # NOTE: 用 except语句捕获弹出的错误类型,并给予命名
    print 'C'
    print x             # NOTE: 打印错误信息

断言 assert 语句
assert 语句用来在程序中引入调试代码
语法:assert 逻辑判断[],表达式]
如果 逻辑判断为真,则不执行任何操作,如果为假,则使用 assert 后的表达式
作为参数实例化 AssertionError 并引发结果实例
assert 的应用领域:
防御性的编程:在发现错误时就停止,防止造成更大的影响
运行时对程序逻辑的检测
合约性检查(比如前置套件,后置条件)
程序中的常量
检查文档.

a = input()
try:
    assert a > 5    # NOTE:  如果a<5 assert 后面的语句不在执行,直接被except 中的AssertionError 捕捉,从而做出反应
    if a>5:
        print 'a>5'
    else:
        print 'a<5'
except AssertionError :
    print 'No assert error'

with...as...语句

语法: with 表达式 as 变量名
表达式 生成一个对象返回给 变量名,如果没有 as 则忽略返回值
用作生成一个临时的变量,在执行完 with 语句后,自动删除 变量名
with...as...语句的执行过程:

class Test(object):
    def __enter__(self):
        print '1.enter...'
    def __del__(self):
        print '3.del...'
    def __exit__(self,type,value,traceback):
        print '4.exit...'
with Test() as Thing:
    print '2.doing something'
print '5.over'
先执行__enter__中的语句
再执行 with中的语句
再执行__del__的语句
最后执行 __exit__的语句
最后执行最后的 print 语句

模块:
模块将程序代码和数据封装起来,以便重复使用,从实际角度来看,一个模块基本上对应一个.py文件,模块导入
其他模块后,就可以带入该模块定义的变量名

模块分为三种:
1.自己写的模块.
2.python官方提供的模块,称为标准库.
3.第三方提供的模块,称为第三方库.
    都可以通过 help('module')来查看库的内容及用法
    一个python工程一般由很多python文件组成,其中每一个文件都可一单独执行,有一个顶层文件,用偶来调用
其他模块,从而控制整个工程的执行流程,
    每个模块都有自己的命名空间,
    在python中,模块也是一个对象
    在一个模块的顶层定义的所有变量(全局变量)都在导入时成为了被导入模块的属性
pyghon中首次导入模块时,会自动执行顶层代码,而函数主体代码直到函数被调用时才会执行,不建议一个非顶层
模块中包含很多类与函数之外的代码
    一个模块被导入时会执行顶层代码,在后续的导入中,不会继续执行,同时,在首次导入的同时,会生成一个
    .pyc格式的字节码文件,

导入模块

1.import 语句
导入指定的模块,
    语法:import module1[,module2...]
    如果 在 module 后加 as X  即可给导入的模块取名为X的别名
    eg: import math as M   即可引入math模块,并取名为X
2.from...import...语句:
    导入而定模块的某一部分属性到当前命名空间,如果有重名的变量,将会被本地变量覆盖.

from A import B      将 模块A中的B属性导入到当前模块中
from A  import *     将 模块A的所有属性都导入到当前模块中,被引入模块的 _C 格式的属性不会被导入

作用:将from后的模块名A中的B导入到当前模块的本地,在使用模块A中的B时,不用写模块A的名称,直接调用即可.

from...import...与 import 的区别:
from A import B 是 导入到本地
import 是导入,调用其属性式,需要在属性名称前加被调用的模块的模块名

模块测试:
如果一个模块被导入,那么这个模块的__name__ 属性是模块的名称,如果是自我
执行的 __name__  属性 为  __main__ 可以用这个方法来进行模块的调试:
if __name__  == __main__:
    测试代码

包:
一个包由多个模块组成,用于将一组模块归并到一个目录中,此目录为包,目录名就是包名,包所提供的层次
对于组织大型系统得的文件会很方便,贱货了模块搜索路径的设置:
包是一个有层次的目录结构,它定义了一个有模块和子包组成的python应用程序执行环境
包的导入吧计算机上的目录变成了另一个命名空间
包的导入:
语法:import dir1.dir2.module1
    导入时目录用 . 来连接各个层次的包,其中,dir1 一定要与导入文件在同一个目录下
包的导入路径内,每个目录下都必须有一个 __init__.py 格式的文件,文件中可以写入代码起到初始化的
作用,也常常为空,这个文件的作用相当于一个挂钩,将各层目录连接起来.
from dir1.dir2.module1 import C
    使用该方式时.模块的调用不需要写路径,直接调用即可.

标准库模块:
    python中有很多标准库,本节介绍几个常用的标准库.
常用的库:
1.sys
sys模块与解释器关系密切,提供了很多函数和变量来处理python运行时环境的不同部分

    sys.argv[] 专门用来向python解释器传递命令行参数
    sys.exit() 用来退出当前程序
    sys.path   查找目录所在的模块
2.os
os模块提供了访问系统服务的功能,模块中的大部分函数通过对应平台相关模块实现,模块会在第一次导入的时候自动加载合适的执行模块,
    os.rename(oldname,newname) 重命名一个文件
    os.remove(filename) 删除一个文件
    os.system(command) 执行系统命令

3.time
    time模块提供了一些处理日期和一天内时间的函数:
    time.time()  获取1970年1月1日0时0分0秒到现在的秒数
    time.localtime() 记录本地时间,使用时间元组来记录,元组记录的信息有:
(年,月,日,小时,分,秒,星期,当年的第几天,是否为夏令时)等9个数据
    time.ctime() 输出时间戳,eg:'Thu Dec  8 10:17:09 2016'
内容有: '星期,月,日,小时:分:秒,年' 等7个数据,比时间戳少了 今年的第几天及是否为夏令时两个数据
    time.asctime() 将时间元组转化为时间戳
    time.mktime()  将时间元组转化为本地时间距离1970年1月1日0时0分0秒的秒数,
    time.clock()   返回一个进程开始运行到现在的时间,以浮点形式体现
    time.sleep()    让程序睡眠多少秒,参数为秒
