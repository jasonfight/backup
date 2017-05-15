### React 的特点
1. React 不是一个完整的MVC框架
1. React跟 Web Componets不冲突
1. React 的特点就是"轻"
1. 组件化的开发思路

### React应用场景

1. 复杂场景下的高性能
1. 重用组件库,组件组合
1. "懒"


### React的使用
1. 需要在html中引入React库文件和Babel库,
1. 在`<script>`标签中,需要设置`type="text/babel"`

### props

props 组件的属性,一般在声明后就不能被改变,props 的拥有者是其创造者

state 私属于当前组件.是可变的.

### 组件的样式的设置:

类的使用,jsx语法中,`class`已经是一个关键字,设置组件的类名时,不能使用`class="..."`的语法来声明,而需要使用`className="..."` 的语法来声明,而同时,类中的各属性名需要使用驼峰法来命名.

在设置行内样式时,同样无法使用`style="..."`的语法,需要使用`style={{...}}`的语法,属性名依然需要使用驼峰法命名.


### React生命周期

1. Mount
  * componentWillMount
  * componentDidMount
1. Update
  * componentWillReceiveProps(接收新的props时被调用)
  * shouldComponentUpdate(接收到新的props和state时,判断是否需要更新DOM结构,如果为true执行componentDidUpdate)
  * componentWillUpdate
  * render
  * componentDidUpdate
1. Unmount
  * componentWillUnmount
