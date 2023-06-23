"""api_dev_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from person_app import views


urlpatterns = [
    path('',views.home,name=""),
    # path('person/', views.person_list, name="person"),
    # path('person/<int:id>', views.person_details),
    path('user-logout/',views.user_logout,name="user-logout"),
    path('user-login/',views.user_login,name="user-login"),
    path('register/',views.register,name='register'),

    #CRUD 
    path('dashboard/',views.dashboard,name="dashboard"),
    # Add a new record
    path('create-record/',views.create_record,name="create-record"),
    # Create a new record
    path('update-record/<int:pk>',views.update_record,name="update-record"),
    # For viewing a singular record
    path('record/<int:pk>',views.singular_record,name="record"),
    # Delete record
    path('delete-record/<int:pk>',views.delete_record,name="delete-record"),
    # Admin dashboard filter options
    path('filter-records/',views.filter_records,name="filter-records"),

]
