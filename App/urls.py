from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('admin_page',views.admin,name='admin')
]
