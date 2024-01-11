from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
from users.models import User
from users.forms import UserProfileForm

def index(request):
    context = {
        'title': 'FutureFood',
            }
    return render(request,'home_page/index.html', context)

def catalog(request, category_id=None, page_number=1):
    catalog = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(catalog, per_page)
    catalog_paginator = paginator.page(page_number)
    if request.user.is_authenticated:
        form = UserProfileForm(instance=request.user)
        context = {
            'form': form,
            'title': 'FutureFood - Catalog',
            'categories': ProductCategory.objects.all(),
            'catalog': catalog_paginator,
            'baskets': Basket.objects.filter(user=request.user),
        }
    else: context = {
            'title': 'FutureFood - Catalog',
            'categories': ProductCategory.objects.all(),
            'catalog': catalog_paginator,
        }
    return render(request, 'catalog_page/catalog.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        if product.allergens.count() >= 1:
            allergy = True
            context = {
                'allergy': allergy,
                'product': product,
                'baskets': Basket.objects.filter(user=request.user),
            }
        else:
            context = {
                'product': product,
                'baskets': Basket.objects.filter(user=request.user),
            }
    else:
         context = {
            'product': product,
         }
    return render(request, 'catalog_page/product_detail.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity+=1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove_all(request):
    basket = Basket.objects.all()
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove_item(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)

    # Проверка наличия товара в корзине перед уменьшением его количества
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        # Если количество товара равно 1, удаляем весь объект корзины
        basket.delete()

    # Редирект обратно на предыдущую страницу
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



