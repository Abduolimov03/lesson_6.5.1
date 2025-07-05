from django.urls import path
from .views import *

urlpatterns = [
    path('kond/', kond_list, name='kond'),
    path('kond/<int:pk>/', kond_detail, name='kond-detail'),
    path('create/', create_kond, name='create-kond'),
    path('update/<int:pk>/', update_kond, name='update-kond'),
    path('del/<int:pk>/', delete_kond, name='del')
]