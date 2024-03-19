from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludito, name='saludito'),
    path('realizar_compra/', views.realizar_compra, name='realizar_compra'),
    path('galletitas/', views.lista_y_detalle_galletitas, name='lista_y_detalle_galletitas'),
    path('recibo/', views.recibo, name='recibo'),
    path('mostrar_historia/', views.mostrar_historia, name='mostrar_historia'),
    path('galletas/', views.detalles_galletas, name='detalles_galletas'),
    path('opinion/', views.opinion_form, name='opinion_form'),
    path('ver-comentarios/', views.ver_comentarios, name='ver_comentarios'),

     
]