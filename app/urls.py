from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('modosit/<int:id>/', views.szakdogaModositas, name = 'modositas'),
    path('torles/<int:id>/', views.szakdogaTorlese, name = 'torles'),
]
