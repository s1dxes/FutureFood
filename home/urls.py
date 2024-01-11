from django.urls import path

from home.views import catalog,product_detail,basket_add,basket_remove,basket_remove_item,basket_remove_all


app_name = 'catalog'
urlpatterns = [
    path('', catalog, name='index'),
    path('baskets/basket_remove_all', basket_remove_all, name='basket_remove_all'),
    path('category/<int:category_id>', catalog, name='category'),
    path('page/<int:page_number>', catalog, name='paginator'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('baskets/add/<int:product_id>', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', basket_remove, name='basket_remove'),
    path('baskets/remove_item/<int:basket_id>', basket_remove_item, name='basket_remove_item'),
]