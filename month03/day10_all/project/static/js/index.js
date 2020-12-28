$(function () {
  // 当页面元素加载完成后执行JS
  console.log(faderData);
  console.log(blogData);

  // 使用外部文件fader.data.js提供的数据faderData
  // 在页面中加载轮播图

  // 图片路径
  // 图片路径通常会随着项目部署位置变化而变化 对于路径而言尽量不要直接写死路径，通常采用当前地址+图片名的方式拼接路径 这样只要部署的位置发生变化 只需要修改当前地址就可以改变所有图片路径
  var BASE_URL = '../static/images/';
  // var server_url = 'http://127.0.0.1:8000/';
  // BASE_URL+'banner01.jpg'

  // 16:05~16:20
  // 遍历faderData 生成三个li标签 拼接到html中
  var html = '';
  $.each(faderData, function (i, o) {
    html += `<li class="slide">
    <a href="#">
    <img src="${BASE_URL + o.img_url}">
    <div class="imginfo">
    ${o.img_info}
    </div>
    </a>
 </li>`
  })
  // 15:55
  // 将html字符串作为兄弟元素添加到页面.fader_controls前面
  $('.fader_controls').before(html);
  // jquery-->easyfader-->index
  // 调用jQuery.easyfader.min.js提供的方法 实现轮播功能
  $('.fader').easyFader();




  // 加载博客列表内容
  // 当页面加载时 先显示4条数据  
  function add_blogs(data) {
    var html = '';
    $.each(data, function (i, o) {
      html += `<div class="blogs">
      <h3 class="blogtitle">
        <a href="#">
          ${o.blogtitle}
        </a>
      </h3>
      <div class="blogpic">
        <a href="#">
          <img src="${BASE_URL + o.blogpic}">
        </a>
      </div>
      <p class="blogtext">
        ${o.blogtext}
      </p>
      <ul>
        <li><a href="#">${o.bloginfo.author}</a></li>
        <li class="lmname">
          <a href="#">${o.bloginfo.lmname}</a>
        </li>
        <li class="timer">
          <a href="#">${o.bloginfo.timer}</a>
        </li>
        <li class="view">
          <a href="#">${o.bloginfo.view}</a>
        </li>
        <li class="like">
          <a href="#">${o.bloginfo.like}</a>
        </li>
      </ul>
    </div>`
    })//each循环结束
    // 将拼接好的内容添加到页面
    $('.blogsbox').append(html);
  }//add_blogs结束

  // slice(start,end)切片操作  从start开始，到end-1位置结束
  add_blogs(blogData.slice(0, 4));

  var canLoad = true;//判断是否可以加载数据
  // 每次用户滚动页面时 如果页面快要到底了 再加载5条数据 直到没有数据为止
  $(document).scroll(function () {
    // console.log('我滚啦')
    // 完整文档高度 整个页面的内容高度
    var documentHeight = $(document).height();
    // 可视范围高度 当前浏览器显示内容的窗口的高度
    var windowHeight = $(window).height();
    // 滚动条高度   滚动条最上方向下滚动的距离
    var scrollHeight = $(document).scrollTop();
    // console.log(documentHeight,windowHeight,scrollHeight)
    if (documentHeight - scrollHeight - windowHeight <= 200) {
      if (canLoad) {
        // 当前一共有多少条数据
        var size = $('.blogs').length;
        // 当前的数据开始再加载5条
        // 页面中有4条数据  slice(4,9)
        // 页面中有9条数据  slice(9,14)
        // 页面中有size条数据 slice(size,size+5)
        var data = blogData.slice(size, size + 5);
        if (data.length > 0) {
          add_blogs(data);
        } else {
          alert('没有数据了')
          canLoad = false;//没有数据后禁止加载
        }
      }

    }
  })


})