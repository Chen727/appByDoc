from django.conf.urls import url
from django.contrib import admin
from polls import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #app的urls里使用如上写法固定polls的名字，然后在Project下的urls里使用include，
    #使用include()可以使URL不限制与地址例如$^，只要include里写对 地址写什么都可以

]