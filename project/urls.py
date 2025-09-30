"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='landing'),
    path('open_form/',views.open_form, name='open_form'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/query/', views.query, name='query'),
    path('dashboard/search/', views.search, name='search'),
    path('dashboard/show_query/', views.show_query, name='show_query'),
    path('dashboard/show_query/update_query/',views.update_query,name='update_query'),
    path('dashboard/show_query/Delete_query/<int:pke>/',views.Delete_query,name='Delete_query'),
    path('log_out/',views.log_out,name='log_out')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)