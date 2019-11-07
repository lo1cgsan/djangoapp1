from django.urls import path
from . import views

app_name = 'studenci'
urlpatterns = [
	path('', views.index, name='index'),
	path('miasta/', views.miasta, name='miasta'),
	path('uczelnie/', views.uczelnie, name='uczelnie'),
	path('login/', views.loguj_studenta, name='login'),
]