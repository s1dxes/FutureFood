from django.shortcuts import render, HttpResponse

from home.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'FutureFood',
        # 'is_promotion': True, 77-81 строка index.html
            }
    return render(request,'home_page/index.html', context)

def catalog(request):
    context = {
        'title': 'FutureFood - Catalog',
        'catalog': Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'catalog_page/catalog.html', context)


# def loss(request):
#     context = {
#         'title': 'FutureFood loss',
#         'is_loss': True,
#             }
#     return render(request,'catalog_page/weight_loss.html', context)
#
# def balance(request):
#     context = {
#         'title': 'FutureFood balance',
#         'is_balance': True,
#             }
#     return render(request,'catalog_page/weight_balance.html', context)
#
# def gain(request):
#     context = {
#         'title': 'FutureFood gain',
#         'is_gain': True,
#             }
#     return render(request,'catalog_page/weight_gain.html', context)