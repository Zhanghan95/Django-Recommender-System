"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('review/', views.review_list, name='review_list'),
    path('', views.movie_list, name='movie_list'),
    path('reviews/<int:pk>', views.review_detail, name='review_detail'),
    path('Movie/',views.movie_list, name='movie_list'),
    path('Movie/<int:pk>', views.movie_detail, name='movie_detail'),
]
