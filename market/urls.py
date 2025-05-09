from django.urls import path
from .views import (
    BbListView, BbCreateView, master, login, register, logout,
    add_to_cart, remove_from_cart, user_cart
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.temp_redirect, name='temp_redirect'),
    path('permanent-redirect/', views.perm_redirect, name='perm_redirect'),
    path('new-page/', views.new_page, name='new_page'),
    path('rubric/<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    # path('', BbListView.as_view(), name='bb_list'),  # Альтернативный вариант списка
    path('add/', BbCreateView.as_view(), name='bb_create'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('index2/', views.HomePageView.as_view(), name='index2'),
    path('about2/', views.AboutPageView.as_view(), name='about2'),
    path('data/', views.DataPageView.as_view(), name='data'),
    path('goiteen/', views.goiteen_form_view, name='goiteen_form'),
    path('master/', master, name='master'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('cart/', user_cart, name='user_cart'),  # Отображение корзины
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),  # Добавление в корзину
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),  # Удаление из корзины
]