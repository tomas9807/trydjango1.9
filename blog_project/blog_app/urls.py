from django.urls import path
from django.views.generic.base import RedirectView
from . import views
app_name = 'posts'
urlpatterns = [
       path('',RedirectView.as_view(url='posts/'), name='home'),
       path('posts/',views.post_list, name='list'),
       path('posts/detail/<int:pk>',views.post_detail, name='detail'),
       path('posts/delete/<int:pk>',views.post_delete, name='delete'),
       path('posts/create',views.post_create, name='create'),
       path('posts/edit/<int:pk>',views.post_update, name='update'),


]