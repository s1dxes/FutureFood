from django.shortcuts import render, HttpResponse



def index(request):
    context = {
        'title': 'FutureFood',
        # 'is_promotion': True, 77-81 строка index.html
            }
    return render(request,'home_page/index.html', context)

def catalog(request):
    context = {
        'title': 'FutureFood - Каталог',
        'products': [
            {'image': '/static/vendor/img/products/food.jpg',
             'name': 'Набор фитоняшка',
             'type': 'Диета',
             'is_loss' : True,
             'price': 700,
             'description': f"1.Овсянка с личи и манго \n"
                            f"2.Ролл с индейкой \n"
                            f'3.Куриный салат с авокадо и грейпфрутом \n'
                            f'4.Десерт "Белый персик \n'
                            f'5.Запеканка из кабачков с курицей \n'
                            f'6.Фруктовый салат с йогуртом \n'
             },
            {'image': '/static/vendor/img/products/food.jpg',
             'name': 'Спорт Лайф Фьюжн',
             'type': 'Баланс',
             'is_balance': True,
             'price': 850,
             'description': "1.Гранола с орехами и фруктами "
                            "2.Салат из тунца и свежих овощей/ Греческий салат "
                            '3.Рататуй с фаршем '
                            '4.Жаркое из индейки с бататом и черносливом '
                            '5.Лосось на пару с лимоном и зеленью/ Куриная грудка с виноградом '
                            '6.Веганский салат из капусты, яблок и семян подсолнечника '
             },
            {'image': '/static/vendor/img/products/food.jpg',
             'name': 'ЭнергоБаланс',
             'type': 'Набор массы',
             'is_gain': True,
             'price': 900,
             'description': f'1. Тост с арахисовым кремом и бананами '
                            f'2.Конверт-ролл "Цезарь" '
                            f'3.Ёжики из индейки и булгура '
                            f'4.Белая рыба в соусе Тикка и бурым рисом '
                            f'5.Свекольный салат с орехами '
                            f'6.Черничное cуфле'
             },
        ]

    }
    return render(request, 'catalog_page/catalog.html', context)



def loss(request):
    context = {
        'title': 'FutureFood loss',
        'is_loss': True,
            }
    return render(request,'catalog_page/weight_loss.html', context)

def balance(request):
    context = {
        'title': 'FutureFood balance',
        'is_balance': True,
            }
    return render(request,'catalog_page/weight_balance.html', context)

def gain(request):
    context = {
        'title': 'FutureFood gain',
        'is_gain': True,
            }
    return render(request,'catalog_page/weight_gain.html', context)