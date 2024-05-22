from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), This would be used to create a separate login page.
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_lead, name='record'),
    #path('add_record/<int:pk>', views.customer_lead, name='record'),
    #path('delete_record/<int:pk>', views.delete_customer_lead, name='delete_record')
]
