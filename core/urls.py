from django.contrib import admin
from django.urls import path

from .views import HomeView  # importamos de views la vista HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pepe/', HomeView.as_view()), # tambien funciona pero igual que en 'admin' se pone 'pepe'
    path('', HomeView.as_view(), name='home'), # mas adelante veremos la ventaja de "name='home'"
]
