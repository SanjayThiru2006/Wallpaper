
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('products/',views.products,name='products'),
    path('logout/', views.logout_view, name='logout'),
    path("live-products/", views.live_products, name="live_products"),
]