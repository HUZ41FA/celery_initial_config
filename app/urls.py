from django.urls import path
from .views import test, test2

app_name = 'app'

urlpatterns = [
    path('test/', test, name = 'test'),
    path('test2/', test2, name = 'test2'),
]
