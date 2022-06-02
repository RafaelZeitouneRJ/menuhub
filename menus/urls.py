from django.urls import path
from . import views

urlpatterns = [
    # retaurant urls
    path('', views.show_restaurants),
    path('new/', views.new_restaurants),
    path('edit/<int:restaurant_id>', views.edit_restaurants),
    path('delete/<int:restaurant_id>', views.delete_restaurants),

    # menu itens urls

    path('menus/<int:restaurant_id>', views.show_menu_itens, name='menu'),
    path('menus/<int:restaurant_id>/new/', views.new_menu_item, name='new'),
    path('menus/<int:restaurant_id>/edit/<int:item_id>',
         views.edit_menu_item, name='edit'),
    path('menus/<int:restaurant_id>/delete/<int:item_id>',
         views.delete_menu_item, name='delete'),

]
