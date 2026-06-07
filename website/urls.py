from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('members/', views.members, name="members"),
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]