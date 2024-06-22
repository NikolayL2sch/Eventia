from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('<int:user_id>/', views.profile, name='profile'),
]