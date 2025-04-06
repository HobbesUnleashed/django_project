"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

# Import the view.py file from the app "as" the function name_view
from hello_world import views as index_views
from about import views as about_views

urlpatterns = [
    # Path of the page (always add the trailing "/"), the view as imported .the name of the function, name it after the function
    path("hello/", index_views.index, name="index"),
    path("about/", about_views.about_me, name="about"),
    path("admin/", admin.site.urls),
]
