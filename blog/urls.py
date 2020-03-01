from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #pk это номер ссылки - порядковое целое число наших постов
    #Параметр post_detail означает, что Django будет искать URL с именем post_detail в файле blog.urls.py
    #Фрагмент post/<int:pk>/ определяет шаблон URL-адреса. Пример - "post/1"
]