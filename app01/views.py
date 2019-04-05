from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

data = []
for i in range(1,301):
    tmp = {'id':i,'name':'anna-{}'.format(i)}
    data.append(tmp)
#data


#def user_list(request):
    #try:
        #page_num = int(request.GET.get('page'))      #字符串类型，转成int
    #except Exception as e:
        #page_num = 1

    #每页十行
    #per_page_num = 10

    #user_list =data[0:10]   1  (1-1)*10    1*10
    #user_list = data[10:20] 2  (2-1)*10    2*10
    #user_list = data[20:30] 3  (n-1)*10    n*10

    #总数据个数
    #total_count =len(data)
    #总共有多少页
    #total_page_num,more=divmod(total_count,per_page_num)
    #if more:
        #total_page_num+=1
    #如果输入的页码数，超过总页数，默认只显示最后一页
    #if page_num>total_page_num:
        #page_num=total_page_num


    #去数据库取数据
    #start = (page_num-1) *per_page_num
    #end = page_num *per_page_num
    #user_list=data[start:end]

    #最多显示多少页码
    #max_show=11
    #half_show=int((max_show-1)/2)

    #页面上页码从哪里开始
    #page_start=page_num-half_show
    #页面上页码最多展示到哪一个
    #page_end=page_num+half_show

    #如果当前页小于等于half_show,默认就从第一页展示到max_show
    #if page_num<=half_show:
        #page_start=1
        #page_end=max_show

    #如果当前页大于等于总页数，减掉half_show
    #if page_num>=total_page_num-half_show:
        #page_end=total_page_num
        #page_start=total_page_num-max_show

    #生成转页码的html
    #page_html_list=[]
    #配置转页码，首页
    #page_first_tmp='<li><a href="/user_list/?page=1">首页</a></li>'
    #page_html_list.append(page_first_tmp)

    #if page_num-1<=0:   #表示没有上一页,class="disabled"使他不能点击
        #page_prev_tmp='<li class="disabled"><a href="#">上一页</a></li>'
    #else:
        #添加  上一页   按钮
        #page_prev_tmp = '<li><a href="/user_list/?page={}">上一页</a></li>'.format(page_num-1)
    #page_html_list.append(page_prev_tmp)

    #for i in range(page_start,page_end+1):
        #如果是当前页，加一个active样式固定住，一个值传两个，{}写上0
        #if i == page_num:
            #tmp = '<li class="active"><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
        #else:
            #tmp = '<li><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
        #page_html_list.append(tmp)

    #if page_num+1>total_page_num:#表示没有下一页,class="disabled"使他不能点击
        #page_next_tmp = '<li class="disabled"><a href="#">下一页</a></li>'
    #else:
         #添加  下一页   按钮
        #page_next_tmp = '<li><a href="/user_list/?page={}">下一页</a></li>'.format(page_num + 1)
    #page_html_list.append(page_next_tmp)

    #添加一个尾页
    #page_last_tmp = '<li><a href="/user_list/?page={}">尾页</a></li>'.format(total_page_num)
    #page_html_list.append(page_last_tmp)

    #page_html=''.join(page_html_list)
    #print(page_html)
    #return render(request,'user_list.html',{'user_list':user_list,'page_html':page_html})


#第二种方法,面向对象的方法
def user_list(request):
    page_num=request.GET.get('page')
    path = request.path_info
    from tools.mypage import MyPage
    page=MyPage(page_num,len(data),path)
    page_html = page.page_html()
    return render(request,"user_list.html",{"user_list":data[page.start:page.end],"page_html": page_html})
