import re

html="""
# <div><p>如果你是大头鬼,那你就fsgedhedgsfdhsfdhdhfdhdhdffhdfhfdhdhhd
# 是彩霞</p></div>
# <div><p>如果你是小头鬼,那你就是晚霞</p></div>

# <div class="animal">
#     <p class="name">
# 			<a title="Tiger"></a>
#     </p>
#     <p class="content">
# 			Two tigers two tigers run fast
#     </p>
# </div>
# 
# <div class="animal">
#     <p class="name">
# 			<a title="Rabbit"></a>
#     </p>
# 
#     <p class="content">
# 			Small white rabbit white and white
#     </p>
# </div>

# <div class="row"><div class="col-md-5"><a href="https://www.biqukan.cc/book/51221/"><img class="thumbnail" src="https://www.biqukan.cc/files/article/image/51/51221/51221s.jpg" alt="万世为王"></a></div><div class="col-md-7 pl0 mb10"><div class="caption"><h4><a href="https://www.biqukan.cc/book/51221/" title="万世为王">万世为王</a></h4><small class="text-muted fs-12">贪睡的龙 / 著</small><p class="text-muted fs-12 hidden-xs"> 再生少年时，重行修行路，既如此，此生当无敌，诸天千域，万世为王！ 微信公众号：贪睡的龙。诚邀亲们关注！ </p></div></div></div>

<div class="movie-item-info">
<p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
<p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>   
     
"""
# pattern='<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>'
# r_list=re.findall(pattern,html,re.S)
# for r in r_list:
#     print('动物名称：',r[0])
#     print('动物描述：',r[1].strip())
pattern='<div class="movie-item-info">.*?data-act="boarditem-click" data-val=.*?>(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?上映时间：(.*?)</p>'
r_list=re.findall(pattern,html,re.S)
for i in r_list:
    print(i[0])
    print(i[1].strip())
    print(i[2])
