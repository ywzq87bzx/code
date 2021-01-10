[TOC]
# 一、 内置对象
  ## 1） 对象
  对象是由属性和方法组成的,使用点语法访问

```js
<script>
    // var obj = {
    //   uname:'qtx',
    //   age:18
    // };
    // console.log(typeof obj);
    // // 获取对象属性的值
    // console.log(obj.uname);
    // console.log(obj['uname']);
    // // 修改属性值
    // obj.age = 20;
    // // 添加属性和值
    // obj.address = '北京';
    // console.log(obj);

    // // 遍历对象
    // for(var i in obj){
    //   console.log(i);//对象的属性 字符串
    //   console.log(obj[i]);
    // }

    // var json = {
    //   "uname":"qtx",
    //   "age":18
    // }
    // console.log(typeof json);//object


    // 构造函数
    // __init__(self)
    // function Dog(color){
    //   this.color = color
    // }

    // var huang = new Dog('yellow'); /new会创建一个全新的对象，会将Dog的属性和方法给到新的对象。
    // console.log(huang,typeof huang);
    // huang.color = 'yello';
    // console.log(huang);
  </script>
```



  ## 2） Array 数组
  #### 1. 创建 
  #### 2. 特点 
+ 数组用于存储若干数据,自动为每位数据分配下标,从0开始
+ 数组中的元素不限数据类型,长度可以动态调整
+ 动态操作数组元素 ：根据元素下标读取或修改数组元素，arr[index]
#### 3. 属性和方法
1. **属性** : length 表示数组长度,可读可写

    ```js
    <script>
        // // 创建数组
        // var arr = [1,2,3,4,5];
        // // 索引
        // // 从0开始依次递增 没有负值
        // console.log(arr[arr.length-1])
        // arr[2] = 3.14;  /修改数组元素
        // console.log(arr);
        // // arr[1:4]     /对象的索引本质是字符串，此处无法转换，错误。
    
        // // Array(5)只写一个参数时表示数组的长度
        // var arr2 = new Array(5);
        // console.log(arr2);//[empty × 5]
        // var arr3 = new Array(1,2,3,4,5);
        // console.log(arr3);//[1,2,3,4,5]
    
     
        var arr = [0,1,2,3,4];
        console.log(arr[5]);//undefined
        arr[5] = 5;
        console.log(arr);
        // arr[10] = 10;
        // console.log(arr);    /中间没有的为空，第十位设置为10，数组可以不连续，可以自由扩展。
      </script>
    ```

2. 方法 :
    + push(data)
    在数组的末尾添加一个或多个元素,多个元素之间使用逗号隔开
    返回添加之后的数组长度

    + pop()
    移除末尾元素
    返回被移除的元素

    + unshift(data)
    在数组的头部添加一个或多个元素
    返回添加之后的数组长度

    + shift()
    移除数组的第一个元素
    返回被移除的元素

    + splice(index,num)

      从数组中添加/删除项目

      返回被删除的项目

    + toString()
    将数组转换成字符串类型
    返回字符串结果

    + join(param)
    将数组转换成字符串,可以指定元素之间的连接符,如果参数省略,默认按照逗号连接
    返回字符串

    + reverse()
    反转数组,倒序重排
    返回重排的数组,注意该方法直接修改原数组的结构

    + sort()
    对数组中元素排序,默认按照Unicode编码升序排列
    返回重排后的数组,直接修改原有数组
    参数 : 可选,自定义排序算法
    	例：
        ```javascript
        //自定义升序
        function sortASC(a,b){
          return a-b;
        }
        ```
       作用：作为参数传递到sort()中,会自动传入两个元素进行比较,如果a-b>0,交换元素的值,自定义升序排列
        ```javascript
        //自定义降序
        function sortDESC(a,b){
        	return b-a;
        }
        //如果返回值>0,交换元素的值,b-a表示降序排列
        ```
```js
<script>
    var arr = [7,23,111,12,54,9]; 默认的arr.sort()会按照字符串的每一位code值排列，但是可以通过定义函数进行排序。
    arr.sort(function(a,b){
      // ab是由sort选择两个传递给匿名函数
      // sort会根据函数的返回值调整ab的顺序 如果返回值大于0 交换ab的位置，否则不变
      // 7-23 不换位置
      // 111-12 换位置
      // 从小到大 升序排列
      // return a-b
        
      // 从大到小 降序排列
      return b-a
    });
    console.log(arr);


    // var arr = [0,1,2,3,4];
    // arr.reverse();   将原来的数组翻转
    // console.log(arr);


    // 转字符串
    // console.log(arr.toString());   
    // var date = [2020,12,1];
    // // console.log(`${date[0]}/${date[1]}/${date[2]}`);
    // console.log(date.join('/'));  将数组转为为指定格式的形式获得。


    // // splice(起始位置，删除数量)
    // var res = arr.splice(1,3); /删除1到3索引的元素
    // console.log(res,arr);
    // // [0,'1',2,3,4]
    // // 从索引值为1的位置开始 删除0个元素 再插入'1',2,3
    // arr.splice(1,0,'1',2,3)
    // console.log(arr);


    // 末尾添加
    // arr.push(5);  /加一个数据到末尾
    // console.log(arr);
    // arr.push(6,7,8);  /加多个数据到末尾
    // console.log(arr);
    // // 末尾移除
    // var res = arr.pop();
    // console.log(res,arr);
    // // 开始添加
    // arr.unshift('0','1','2');
    // console.log(arr)
    // // 开始移除
    // arr.shift()
    // console.log(arr);
  </script>
```



#### 4. 二维数组 

数组中的每个元素又是数组
```javascript
 var arr1 = [1,2,3];
 var arr2 = [[1,2],[3,4],[5,6,7]];
 //操作数组元素
 var r1 = arr2[0] //内层数组
 var num = r1[0]; //值 1
 //简写
 var num2 = arr2[1][0];
```
## 3）String 对象
#### 1. 创建 
```javascript
    var str = "100";
    var str2 = new String("hello");
 <script>
     
    var str = 'abcde';
    // var str2 = new String('abcde');
    console.log(str);
    // console.log(str2);
    console.log(str[0]);
    // str[0] = 'A';
    console.log(str);

    // 遍历数组/字符串
    for(var i=0;i<str.length;i++){
      console.log(str[i]);
    }

    for(var i in str){
      console.log(i,str[i]);//i索引值
    }
  </script>
```
#### 2. 特点 
字符串采用数组结构存储每位字符,自动为字符分配下标,从0开始
#### 3. 属性 
length ：获取字符串长度
#### 4. 方法 
+ 转换字母大小写
    toUpperCase() 转大写字母
    toLowerCase() 转小写字母
    返回转换后的字符串,不影响原始字符串

+ 获取字符或字符编码
    charAt(index)	   获取指定下标的字符
    charCodeAt(index)  获取指定下标的字符编码
    参数为指定的下标,可以省略,默认为0

+ 获取指定字符的下标

    + indexOf(str,fromIndex)
    作用 : 获取指定字符的下标,从前向后查询,找到即返回
    参数 :
    	str 表示要查找的字符串,必填
    	fromIndex 表示起始下标,默认为0
    返回 :
    	返回指定字符的下标,查找失败返回-1

+ 截取字符串
    substring(startIndex,endIndex)
    作用 : 根据指定的下标范围截取字符串,startIndex ~ endIndex-1
    参数 :
     startIndex	表示起始下标
     endIndex	表示结束下标,可以省略,省略表示截止末尾

+ substr(startIndex,len)

    作用：根据下标截取指定的字符串

+ 分割字符串
    split(param)
    作用 : 将字符串按照指定的字符进行分割,以数组形式返回分割结果
    参数 : 指定分隔符,必须是字符串中存在的字符,如果字符串中不存在,分割失败,仍然返回数组

    ```js
    <script>
        var str = 'This is a test string';
    
        //截取字符串 
        str.substr(10,4)//"test"
        str.substring(10,14)//"test"
    
    
        // str.charAt(10)//'t'
        // str.charCodeAt(8)//97
    
        // str.indexOf('a')//8
        // str.indexOf('x')//-1
    
    
        //转换大小写,不修改原本内容
        // console.log(str.toUpperCase());
        // console.log(str.toLowerCase());
        // console.log(str);
      </script>
    ```
    
    ```js
    <body>
      <input id="email" type="text" placeholder="请输入邮箱">
      <button id="btn">解析</button>
      <h1 id="show">xxx</h1>
    
      <script>
        // 查找页面元素
        var btn = document.getElementById('btn');
        var email = document.getElementById('email');
        var show = document.getElementById('show');
    
        // 当用户点击按钮解析时 
        btn.onclick = function(){
          // 获取用户输入的邮箱 从邮箱中解析出用户名和服务商
          // 'shibw@tedu.cn'
          var str = email.value;
          var arr = str.split('@');
          console.log(arr);//["shibw", "tedu.cn"]
          show.innerHTML = `用户名：${arr[0]},服务商：${arr[1]}`
    
          // var index = str.indexOf('@');
          // var u = str.substring(0,index);
          // var f = str.substring(index+1);
          // 将结果放到页面中显示
          // show.innerHTML = `用户名：${u},服务商：${f}`;
        }
    
        // shibw@tedu.cn 获取用户名和服务商
        // 用户名:shibw 
        // 服务商:tedu.cn
        // var emial = 'qtx@tedu.cn';
        // // substring()
        // // 获取@的索引值index indexOf()
        // var index = emial.indexOf('@');
        // console.log(index);
        // // 从0～index 用户名  从index+1~末尾 服务商
        // var u = emial.substring(0,index);
        // var f = emial.substring(index+1);
        // console.log(`用户名：${u},服务商：${f}`);
    
      
    
      </script>
    ```
    
    
    
+ 模式匹配
  
+ 正则表达式对象 RegExp
  
    RegExp : Regualr Expression
    
    1. 语法 ：
       var reg1 = /微软/ig;
       var reg2 = new RegExp('匹配模式','修饰符');
       正则表达式对象可以接收一个变量。
    
	2. 属性 ：
    
       lastIndex : 可读可写，表示下一次匹配的起始索引
       注意 ：
    
       1. 默认情况下，正则表达式对象不能重复调用方法，
          如果重复调用，结果会出错：
          由于 lastIndex 保存再一次匹配的起始下标，
          重复调用时，不能保证每次都从下标0开始
          验证，可以手动调整 lastIndex 为 0。
       2. 只有正则对象设置全局匹配 g ，该属性才起作用。
    
    3. 方法 ：
    
       test(str) :验证字符串中是否存在满足正则匹配模式的内容，存在则返回true，
    
       不存在返回false参数为要验证的字符串。
    
+ 作用 : 借助正则表达式实现字符串中固定格式内容的查找和替换
    正则表达式 :
     var reg1 = /字符模式/修饰符;
     修饰符 : 
      i :  ignorecase 忽略大小写
      g : global 全局范围
    字符串方法 :
    
    + match(regExp/subStr)
	作用 : 查找字符串中满足正则格式或满足指定字符串的内容
    	返回 : 数组,存放查找结果
    	
    + replace(regExp/subStr,newStr)
      作用 : 根据正则表达式或字符串查找相关内容并进行替换
      返回 : 替换后的字符串,不影响原始字符串。
      
      ```js
       <script>
      
          var str = 'This is a test string';
          var reg = /is/ig;
          var reg2 = new RegExp('this','ig');
          // console.log(reg,reg2);
          console.log(reg.test(str));
      
          //字符串的查找和替换
          var res = str.match(reg);
          console.log(res);
      
          var newStr = str.replace(reg,'at');
          console.log(newStr);
          console.log(str);
        </script>
      ```
      
      ```
      <body>
        <input id="phone" type="text" placeholder="请输入手机号">
        <span id="show">xxx</span>
        <script>
          // 当用户输入完手机号以后 
          // 检测手机号的格式是否正确
          var phone = document.getElementById('phone');
          var show = document.getElementById('show');
          // console.log(show)
          phone.onchange = function(){
            // 获取用户输入的手机号
            var str = phone.value;
            // 检测格式
            var reg = /^1[34578]\d{9}$/;
            // console.log(reg.test(str));
            if(reg.test(str)){
              show.innerHTML = '手机号格式正确';
            }else{
              show.innerHTML = '手机号格式有误';
            }
          }
          // innerHTML前面内容没找到
          // null没有innerHTML这个属性
          // Uncaught TypeError: Cannot set property 'innerHTML' of null
      
      
          // onfocus 获取焦点
          // onblur 失去焦点
          // phone.onfocus = function(){
          //   console.log('hello world');
          // }
      
          // onchange 值发生改变
          // phone.onchange = function(){
          //   console.log('hello world');
          // }
      
          // oninput 输入事件
          // phone.oninput = function(){
          //   console.log('hello world');
          // }
        </script>
      </body>
      ```
      
      

## 4)  Math 对象

#### 1. 定义

Math对象主要提供一些列数学运算的方法

#### 2. 属性

1. 圆周率 :  Math.PI
2. 自然对数 : Math.E

#### 3. 方法

1. Math.random();   生成0-1之间的随机数

2. Math.ceil(x);	     对x向上取整,忽略小数位,整数位+1

3. Math.floor(x);      对x向下取整,舍弃小数位,保留整数位

4. Math.round(x);    对x四舍五入取整数

   ```js
   <body>
     <script>
       
       // console.log(Math.random());
   
       // 将随机数放入变量中保存方便后续使用
       // var num = Math.random();
       // console.log(num);//0~1
       // console.log(Math.ceil(num));
       // console.log(Math.floor(num));
       // console.log(Math.round(num));
   
       // 0~3之间的随机整数
       // var num = Math.random()*3;
       // console.log(num);
       // console.log(Math.ceil(num));//1~3
       // console.log(Math.floor(num));//0~2
       // console.log(Math.round(num));//0~3
   
       // 使用向下取整的方式实现0~3
       Math.floor(Math.random()*4)
       // 0~n之间的随机整数
       // Math.floor(Math.random()*(n+1))
   
       // 使用向下取整的方式实现1~3
       Math.floor(Math.random()*3)+1
       // 2~10之间的随机整数
       Math.floor(Math.random()*9)+2
       // 5~10
       Math.floor(Math.random()*6)+5
       // 1~n之间的随机整数
       // Math.floor(Math.random()*n)+1
       // m~n之间的随机整数
       // Math.floor(Math.random()*(n+1-m))+m
     </script>
   </body>
   ```

   ```js
   随机在画面中显示4张图片排列(但是会有重复）：
    <title>Document</title>
     <style>
       ul,li {
         margin: 0;
         padding: 0;
         list-style: none;
         float: left;
       }
     </style>
   </head>
     <body>
     <!-- ul>li*4>img -->
     <ul>
       <li><img src="../imgs/bk0-8.jpg" alt=""></li>
       <li><img src="../imgs/bk1-8.jpg" alt=""></li>
       <li><img src="../imgs/bk2-8.jpg" alt=""></li>
       <li><img src="../imgs/bk3-8.jpg" alt=""></li>
     </ul>
   
     <script>
       // 生成0～9之间的随机数
       // 使用随机生成一个路径 `../imgs/bk${num}-8.jpg`
       // 将生成的内容添加到数组
       var arr = []
   
       for (var i = 0; i < 4; i++) {
         var num = Math.floor(Math.random() * 10);
         var url = `../imgs/bk${num}-8.jpg`;
         arr.push(url);
       }
       // 根据数组中的内容在页面中显示图片
       // 通过标签名查找页面img
       var imgs = document.getElementsByTagName('img');
       // 遍历取到每一个页面元素 然后修改src属性值
       for (var i = 0; i < imgs.length; i++) {
         imgs[i].src = arr[i];
       }
   
     </script>
   </body>
   ```

   ```
    <style>
       ul,
       li {
         margin: 0;
         padding: 0;
         list-style: none;
         float: left;
       }
     </style>
   </head>
   
   <body>
     <ul>
       <li><img src="../imgs/bk0-8.jpg" alt=""></li>
       <li><img src="../imgs/bk1-8.jpg" alt=""></li>
       <li><img src="../imgs/bk2-8.jpg" alt=""></li>
       <li><img src="../imgs/bk3-8.jpg" alt=""></li>
     </ul>
   
     <script>
       // 09:52~10:07
       // var arr = []
       // while(arr.length<4){
       //   var num = Math.floor(Math.random() * 10);
       //   var url = `../imgs/bk${num}-8.jpg`;
       //   // 判断数组中是否有相同的url
       //   if(arr.indexOf(url) == -1){
       //     arr.push(url);
       //   }
       //   // var has = false;//默认没有
       //   // for(var i=0;i<arr.length;i++){
       //   //   if(arr[i] == url){
       //   //     has = true//如果遍历到相同内容 改成true
       //   //   }
       //   // }
       //   // if(has){
       //   //   continue
       //   // }
       // }
   
   
       var arr = [
       "../imgs/bk0-8.jpg","../imgs/bk1-8.jpg",
       "../imgs/bk2-8.jpg","../imgs/bk3-8.jpg",
       "../imgs/bk4-8.jpg","../imgs/bk5-8.jpg",
       "../imgs/bk6-8.jpg","../imgs/bk7-8.jpg",
       "../imgs/bk8-8.jpg","../imgs/bk9-8.jpg"
       ]
       // 打乱数组顺序
       arr.sort(function(){
         // 如果值为正数就换位置
         return Math.random()-0.5
       })
   
       var imgs = document.getElementsByTagName('img');
       for (var i = 0; i < imgs.length; i++) {
         imgs[i].src = arr[i];
       }
   
     </script>
   </body>
   ```

   

## 5）日期对象

#### 1. 创建日期对象

      1. var date2 = new Date("2011/11/11");
      2. var date3 = new Date("2011/11/11 11:11:11");

#### 2. 日期对象方法

1. 读取或设置当前时间的毫秒数：getTime()
2. 获取时间分量
   - getFullYear()
   - getMonth()
   - getDate()

```js
<body>
  <h1 id="show"></h1>
  <script>
    var now = new Date();
    var noon = new Date('2020-12-04 12:00:00');
    // console.log(noon-now);
    // ms-->s  1000ms=1s
    var leftTime = parseInt((noon - now)/1000);
    // 时间差
    console.log(leftTime);
    // 通过时间差求 时 分 秒
    // 显示距离中午12点还有xx时xx分xx秒
    var hours = parseInt(leftTime/3600);
    var minutes = parseInt(leftTime/60%60);
    var seconds = leftTime % 60;
    // 如果时分秒的值是一位数字 补0变成两位数字
    // 10:55~11:10  1 --> 01   '0'+1
    function addZero(num){
      // if(num<10){
      //   return '0'+num;
      // }else{
      //   return num.toString();
      // }
      return num<10?'0'+num:num+'';
    }
    show.innerHTML = `距离中午12点还有${addZero(hours)}时${addZero(minutes)}分${addZero(seconds)}秒`


    // 当前的时间日期
    // var now = new Date();
    // console.log(now);
    // var end = new Date(2020,1,1);
    // var end = new Date('2020/1/1');
    // console.log(end);
    // now.getFullYear()//年
    // now.getMonth()//月0~11
    // now.getDate()//日期
    // now.getDay()//星期
    // now.getHours()//时
    // now.getMinutes()//分
    // now.getSeconds()//秒
    // now.getMilliseconds()//毫秒  1000ms = 1s
    // now.getTime()//时间戳
    
  </script>
</body>
```

