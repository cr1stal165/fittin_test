"""
URL configuration for fittin_test project.

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

from cart.views import CartList, CartAddProducts, CartEditProducts, CartDeleteProduct
from category.views import CategoryTreeList
from order.views import OrderCreate
from product.views import ProductCategoryFiltering, ProductList
from fittin_test.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('products', ProductCategoryFiltering.as_view(), name='products'),
    path('product', ProductList.as_view()),
    path('cart', CartList.as_view()),
    path('cart/add', CartAddProducts.as_view()),
    path('cart/edit', CartEditProducts.as_view()),
    path('cart/delete', CartDeleteProduct.as_view()),
    path('order/', OrderCreate.as_view()),
    path('categories/', CategoryTreeList.as_view(), name='category-list'),
]

urlpatterns += doc_urls
