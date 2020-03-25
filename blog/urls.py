from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),

    #pk это номер ссылки - порядковое целое число наших постов
    #Параметр post_detail означает, что Django будет искать URL с именем post_detail в файле blog.urls.py
    #Фрагмент post/<int:pk>/ определяет шаблон URL-адреса. Пример - "post/1"
]