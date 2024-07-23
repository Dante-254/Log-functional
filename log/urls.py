from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login.html', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('tables', views.tables, name='tables' )

]
