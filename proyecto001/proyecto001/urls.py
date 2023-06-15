from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [

path('admin/', admin.site.urls),
path('', views.index, name = "index"),
path('inicio/', views.index, name = "inicio"),
path('saludo/',views.saludo, name = "saludo"),
path('rango/',views.rango,name="rango"),
path('rango2/',views.rango2,name="rango2"),
path('rango2/<int:a>',views.rango2,name="rango2"),
path('rango2/<int:a>/<int:b>',views.rango2,name="rango2"),

]