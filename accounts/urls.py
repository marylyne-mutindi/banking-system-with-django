from django.urls import path
from . import views
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_account, name='create_account'),
    path('access/', views.access_account, name='access_account'),
    path('deposit/<str:acc_no>/', views.deposit, name='deposit'),
    path('withdraw/<str:acc_no>/', views.withdraw, name='withdraw'),
path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/<str:acc_no>/', views.user_dashboard, name='user_dashboard'),

]
