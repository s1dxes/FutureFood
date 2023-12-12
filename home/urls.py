from django.urls import path
from home.views import catalog

app_name = 'catalog'
urlpatterns = [
    path('', catalog, name='index'),
]