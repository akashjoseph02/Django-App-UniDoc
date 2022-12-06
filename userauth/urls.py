from django.urls import path

from . import views

app_name = 'userauth'

urlpatterns = [
    path('login/', views.t_login, name='login'),
    path('signup/', views.t_sign_up, name='signup' ),
    path('logout/', views.logoutUSer,name='logout')
]