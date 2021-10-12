from django.urls import path

from . import views

 

urlpatterns = [

    path('',views.mypage,name='mypage'),
    path('add', views.add,name='add'),
    path('register', views.register,name='register'),
    path('show', views.show,name='show'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),




]