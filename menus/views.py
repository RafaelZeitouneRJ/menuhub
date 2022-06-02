
from django.shortcuts import render, redirect
from menus.models import MenuItem, Restaurant

# Create your views here.


def show_restaurants(request):
    """ Show restaurants by name """
    restaurants = Restaurant.objects.order_by('name')
    context = {'restaurants': restaurants}
    return render(request, "restaurants/show_restaurants.html", context)


def edit_restaurants(request, restaurant_id):
    """edit a restaurant by a id."""
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        form_data = request.POST
        restaurant.name = form_data.get('name')
        restaurant.save()
        return redirect("/")
    else:
        return render(request, "restaurants/edit_restaurants.html", {'restaurant': restaurant})


def show_menu_itens(request, restaurant_id):
    """ Show a menus by category for a restaurant """
    menu_itens = MenuItem.objects.filter(
        restaurant_id=restaurant_id).order_by('category')
    context = {'restaurants': restaurant_id, 'menu_itens': menu_itens}
    return render(request, "menus/show_menu_itens.html", context)


def new_menu_item(request, restaurant_id):
    """Create a new menu item for restaurant"""
    if request.method == 'POST':
        form_data = request.POST
        menu_item = MenuItem()
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.restaurant_id = restaurant_id
        menu_item.save()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, "menus/new_menu_itens.html", {'restaurant_id': restaurant_id})
