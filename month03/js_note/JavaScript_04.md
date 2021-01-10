[TOC]
# 一、BOM 对象
## 1. BOM 介绍 
​		BOM全称为“Browser Object Model”，浏览器对象模型。提供一系列操作浏览器的属性和方法。核心对象为window对象，不需要手动创建，跟随网页运行自动产生，直接使用，在使用时可以省略书写。
## 2. 对象方法
1. ##### 网页弹框

   ```javascript
   alert()		//警告框
   confirm()	//确认框
   <body>
   
     <script>
       // var arr = [10,3.14,'hello wrold',{'name':'qtx'},[1,2,3]];
       // var res = arr.indexOf(2020);
       // console.log(res);
       // var res = confirm('确定要删除吗？');
       // alert(res);
     </script>
   </body>
   ```

2. ##### 定时器方法

![setInterval函数2](assets\setInterval函数2.png)

**周期性定时器**
	作用：每隔一段时间就执行一次代码

```javascript
//开启定时器:
var timerID = setInterval(function,interval);
/*
参数 :
 function : 需要执行的代码,可以传入函数名;或匿名函数
 interval : 时间间隔,默认以毫秒为单位 1s = 1000ms
返回值 : 返回定时器的ID,用于关闭定时器
*/
```
   关闭定时器 :
```javascript
//关闭指定id对应的定时器
clearInterval(timerID);
```
![setTimeout函数3](assets\setTimeout函数3.png)

**一次性定时器**
	作用：等待多久之后执行一次代码

```javascript
//开启超时调用:
var timerId = setTimeout(function,timeout);
//关闭超时调用:
clearTimeout(timerId);
```
```js
<body>
  <button id="btn1">创建周期性定时器</button>
  <button id="btn2">停止周期性定时器</button>
  <script>
    var timerId = null;   //防止同时点击多次定时器
    btn1.onclick = function () {
      // 如果没有相同的定时器  创建定时器
      if (timerId == null) {
        // 创建周期性定时器
        // 将timerId变成全局变量 方便停止时使用
        timerId = setInterval(function () {
          console.log('hello world');
        }, 1000);
      }
    }
    btn2.onclick = function () {
      // 停止周期性定时器
      clearInterval(timerId);
      timerId = null;//清空变量
    }
  </script>

  <script>
    //一次性定时器
    var timer = setTimeout(function(){
      alert('hello world')
    },3000);
    clearTimeout(timer);
  </script>
</body>
```

```js
//页面小广告
 <title>页面小广告</title>
  <style>
    div {
      width: 122px;
      /* border: 5px solid red; */
      position: fixed;
      right: -123px;
      top: 50%;
      margin-top: -150px;
      transition: all 1s;
    }
  </style>
</head>


<body>
  <div id="parent">
    <img id="main" src="../imgs/img02-5.png" alt="">
    <img id="close" src="../imgs/img01-5.png" alt="">
  </div>
  <script>
    var parent = document.getElementById('parent')
    setTimeout(function () {
      // 通过style属性修改样式
      parent.style = "right: 0";
    }, 2000);

    // 点击关闭隐藏元素
    var close = document.getElementById('close');
    close.onclick = function () {
      parent.style = "right:-123px";
      setTimeout(function () {
        parent.style = "right: 0";
      }, 5000);
    }
  </script>
</body>
```



## 3. 对象属性

window的大部分属性又是对象类型

1. ##### history

   作用：保存当前窗口所访问过的URL
   属性 :  length 表示当前窗口访问过的URL数量
   方法 :

   ```javascript
   back() 对应浏览器窗口的后退按钮，访问前一个记录
   forward() 对应前进按钮，访问记录中的下一个URL
     <a href="history.html">历史记录页面</a>
     <button onclick="history.forward()">
       前进
     </button>
     <button onclick="history.back()">
       后退
     </button>
   ```

2. ##### location

   作用：保存当前窗口的地址栏信息(URL) 
   属性 :  href 设置或读取当前窗口的地址栏信息
   方法 :

   ```text
   reload(param) 重载页面(刷新)
   参数为布尔值，默认为 false，表示从缓存中加载，设置为true,强制从服务器根目录加载
   ```

```js
<title>location</title>
</head>
<body>
  <h1>三秒钟后跳转到百度...</h1>
  <!-- <a href="http://www.baidu.com"></a> -->
  <script>
    // location.reload();

    // console.log(location.href);
    setTimeout(function(){
      location.href = "http://www.baidu.com"
    },3000)
  </script>
</body>
```



# 二、DOM节点操作

DOM全称为 “Document Object Model”，文档对象模型，提供操作HTML文档的方法。（注：每个html文件在浏览器中都视为一篇文档,操作文档实际就是操作页面元素。）
## 1. 节点对象

JavaScript 会对 html 文档中的元素、属性、文本甚至注释进行封装，称为节点对象，提供相关的属性和方法。

## 2. 访问节点

- 元素节点   ( 操作标签）
- 属性节点（操作标签属性）
- 文本节点（操作标签的文本内容）

标签属性都是元素节点对象的属性,可以使用点语法访问，例如：

```javascript
h1.id = "d1"; 		 //set 方法
console.log(h1.id);  //get 方法
h1.id = null;		//remove 方法
```

注意 :

- 属性值以字符串表示
- class属性需要更名为 className，避免与关键字冲突，例如：
  h1.className = "c1 c2 c3"；

## 3. 操作元素样式

1. 为元素添加 id、class属性，对应选择器样式
2. 操作元素的行内样式，访问元素节点的style属性，获取样式对象；样式对象中包含CSS属性，使用点语法操作。

```javascript
p.style.color = "white";
p.style.width = "300px";
p.style.fontSize = "20px";
```

注意 :

- 属性值以字符串形式给出，单位不能省略

- 如果css属性名包含连接符，使用JS访问时，一律去掉连接符,改为驼峰， font-size -> fontSize

  ```js
  <title>Document</title>
    <style>
      .red{
        width: 200px;
        height: 200px;
        background-color: red;
      }
    </style>
  </head>
  <body>
  
    <div id="d1"></div>
    <script>
      var d1 = document.getElementById('d1');
      d1.className = 'red';
  
      // d1.style.width = '200px';
      // d1.style.height = '200px';
      // d1.style.backgroundColor = 'red';
  
      // d1.style = 'width:200px;height:200px;background-color:red';
      // console.log(d1.style)
  
  
  
      // 查找页面元素
      // document.getElementById()
      // document.getElementsByClassName()
      // document.getElementsByTagName()
  
  
      // 操作页面元素(对象)
      // 对属性的操作
      // 对象.属性      获取对象的属性值
      // 对象.getAttribute(属性名)
  
      // 对象.属性=值   设置对象的属性
      // 对象.setAttribute(属性名，属性值)
  
      // 对象.属性=''   清空对象的属性
      // 对象.removeAttribute(属性名)
  
      // 对内容的操作
      // 对象.innerHTML  获取内部的HTML内容
      // 对象.innerText  获取内部的文本内容
      // 对象.value      获取表单控件的值
  
      // 对样式的操作
      // 对象.style=值
    </script>
  </body>
  ```

  ```javascript
  <title>导航条</title>
    <style>
      /* 清除默认样式 */
      a{
        color: #222;
        text-decoration: none;
      }
      ul{
        margin: 0;
        padding: 0;
        /* 清除列表样式 小圆点 */
        list-style: none;
        border: 1px solid red;
        /* 解决子元素浮动父元素没有高度的问题 */
        overflow: hidden;
      }
      /* 10:00~10:15 */
      li{
        float: left;
      }
      .first{
        color: #999;
        margin: 5px 0; 
      }
      .item{
        margin: 5px 10px;
        padding: 0 5px;
      }
      .active,.item:hover{
        background-color: red;
      }
      .active>a,.item:hover>a{
        color: #fff;
      }
    </style>
  </head>
  <body>
    <ul>
      <li class="first">难度：</li>
      <li class="item"><a href="#">全部</a></li>
      <li class="item"><a href="#">初级</a></li>
      <li class="item active">
        <a href="#">中级</a>
      </li>
      <li class="item"><a href="#">高级</a></li>
    </ul> 
    <script>
      // day04/nav.html
      // 当每一个li被鼠标单击时 显示hello world
      // 查找页面元素 .item
      // 遍历页面元素为每一个添加事件
      var items = document.getElementsByClassName('item');
      console.log(items);
      for(var i=0;i<items.length;i++){
        items[i].onclick = function(){
          // console.log('hello world');
          // this指调用函数的对象 当前对象
          // console.log(this);
          // 遍历元素 清除所有元素的active样式
          for(var j=0;j<items.length;j++){
            items[j].className = 'item';
          }
          // 为自己添加active样式
          this.className = 'item active';
        }
      }
    </script>
  </body>
  ```

  ```javascript
   <title>倒计时</title>
  </head>
  
  <body>
    <h1 id="show"></h1>
    <script>
      // 根据date.html 实现距离18:00的倒计时
      // 当前时间 
      // 结束时间
      // 计算时间差
      // 求时分秒 补0
      // 在页面中显示
      function addZero(num) {
        return num < 10 ? '0' + num : num + '';
      }
      function countDown() {
        var now = new Date();
        var end = new Date('2020-12-04 18:00:00');
        var leftTime = parseInt((end - now) / 1000);
        // 判断时间是否过去了
        if (leftTime <= 0) {
          show.innerHTML = '来晚啦 活动已经过去了';
          clearInterval(timer);
          return
        }
        var hours = parseInt(leftTime / 3600);
        var minutes = parseInt(leftTime / 60 % 60);
        var seconds = leftTime % 60;
        show.innerHTML = `距离18点还有${addZero(hours)}时${addZero(minutes)}分${addZero(seconds)}秒`
      }
      countDown();
      // 实现自动计时 setInterval()
      var timer = setInterval(countDown, 1000);
      // 如果时间超过18:00  停止计时
    </script>
  </body>
  ```

  ```javascript
   <title>轮播图</title>
    <style>
      ul {
        position: relative;
        margin: 0;
        padding: 0;
        list-style: none;
        border: 5px solid red;
        width: 739px;
        height: 419px;
      }
      .pager{
        position: absolute;
        top: 0;
        left: 0;
        /* 不透明度0(透明)～1(不透明) */
        opacity: 0;
        transition: all 0.5s;
      }
      .active{
        opacity: 1;
      }
      #ll,#rr{
        position: absolute;
        top:50%;
        margin-top:-20px;
      }
      #rr{
        right: 0;
      }
    </style>
  </head>
  
  <body>
    <ul>
      <li>
        <img class="pager active" src="../imgs/gm1-6.jpg">
      </li>
      <li>
        <img class="pager" src="../imgs/gm2-6.jpg">
      </li>
      <li>
        <img class="pager" src="../imgs/gm3-6.jpg">
      </li>
      <li>
        <img class="pager" src="../imgs/gm4-6.jpg">
      </li>
      <li>
        <img class="pager" src="../imgs/gm5-6.jpg">
      </li>
  
      <li>
        <img id="ll" src="../imgs/l1-6.png" alt="">
        <img id="rr" src="../imgs/r1-6.png" alt="">
      </li>
    </ul>
  
  
    <script>
      // 查找页面元素
      // 左右箭头按钮
      var ll = document.getElementById('ll');
      var rr = document.getElementById('rr');
      // 所有的轮播图片
      var pagers = document.getElementsByClassName('pager');
  
      var i = 0;//当前图片的索引值
      rr.onclick = function(){
        // 向右切换
        // 0 1 2 3 4 0 1 2...
        // 清除当前图片的class active
        pagers[i].className = 'pager'
        // 确定下一张图片的位置
        i++;
        if(i==pagers.length){
          i=0;
        }
        // 为下一张图片添加class active 
        pagers[i].className = 'pager active'
      }
  
      // 实现向左切换图片
      // 实现自动向右切换图片
      // 实现鼠标移入图片停止定时器 鼠标移出启动定时器
      // onmouseover 鼠标移入
      // onmouseout 鼠标移出
    </script> 
  </body>
  ```

  