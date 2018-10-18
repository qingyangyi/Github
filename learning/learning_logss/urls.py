"""定义learning_logss的URL模式"""
from django.urls import re_path,include
from . import views
"""
下面是官方文档的内容，如果在urls.py中使用到正则匹配路径（^$）的时候，
就需要使用re_path,而不能使用path，不然页面会显示404错误
"""
app_name = 'learning_logss'#记得注册命名空间，否则报not register
urlpatterns =[
    #主页
    re_path(r'^$',views.index,name='index'),
    re_path(r'^topics/$',views.topics,name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry')
    ]
