
from django.urls import path
from .views import articles_list

app_name = 'articles'

urlpatterns = [
    path('', articles_list, name='articles'),
]
