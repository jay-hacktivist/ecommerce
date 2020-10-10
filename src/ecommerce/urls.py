"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import home_page, about_page, contact_page, login_page, register_page

from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

urlpatterns = [
    path('', home_page, name="homepage"),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('products/', ProductListView.as_view(), name="products"),
    path('products-fbv/', product_list_view, name="products-fbv"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('products-fbv/<int:pk>/', product_detail_view, name="detail-fbv"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)