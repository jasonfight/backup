## React 原理

### React组件更新原理

React中的组件不是真实的DOM节点, 而是存在于内存之中的一种数据结构, 叫做虚拟DOM(virtual DOM). 只是当它插入文档以后, 才会变成真实的DOM. 根据React的设计, 所有的DOM变动, 都先在虚拟DOM上发生, 然后再将实际发生变动的部分, 反映在真实DOM上, 这种算法叫做DOM diff, 这样可以大大提高网页的性能表现.

### React的5个生命周期


1. componentWillMount():在渲染之前调用,在客户端也在服务端
1. componentDidMount():在加载之后调用,只在客户端,之后组件已经生成了对应的DOM结构,可以通过`this.getDOMNode()`来进行访问,
如果要和其他`JavaScript`框架一起使用,可以在这个方法中调用`setInterval`,`setTimeout`或者发送`AJAX`请求等操作
1. componentWillUpdate():在组件接受到一个新的`props`时被调用,这个方法在加载时不会被调用
1. componentDidUpdate():返回一个布尔值,在组件接收到新的`props`或者`state`时被调用,在加载时或`forceUpdate`时不被调用
1. componentWillUnmount():在组件从`DOM`中移出的时候被立即调用.


### props与state的区别
  this.props表示那些一旦定义, 就不再改变的特性, 而this.state是会随着用户互动而产生变化的特性.





