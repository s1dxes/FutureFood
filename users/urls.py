from django.urls import path
from users.views import login, registration, profile, bmi_history
from django.contrib.auth.views import LogoutView


app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('bmi_history/', bmi_history, name='bmi_history'),
    path('logout/', LogoutView.as_view(), name='logout'),
]