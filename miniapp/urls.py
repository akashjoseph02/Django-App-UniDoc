from django.urls import path

from . import views

app_name = 'miniapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.appview, name="dashboard"),
    path('booking', views.booking, name='booking'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
]