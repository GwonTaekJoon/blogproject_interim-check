#원래 app안에는 urls.py라는 파일이 없으나 개별적인 관리를 위해 include하고 파일을 생성해준겁니다.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name = "home"),
    path('newblog/', views.create, name = "newblog"), # funccrud/newblog 형태의 url생성
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add_comment/<int:pk>', views.add_comment, name='add_comment'),
    path('blog/<int:blog_id>',views.detail,name="detail"),
]