from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guardar/', views.guardarEvento, name='guardar_evento'),
    path('guardarRegistro/', views.guardarRegistro, name='guardarRegistro'),
    path('eliminar/<str:titulo>/', views.eliminarEvento, name='eliminar_evento'),
    path('eliminarRegistro/<int:registro_id>/', views.eliminarRegistro, name='eliminarRegistro'),
    path('editarEvento/<str:titulo>/', views.editarEvento, name='editarEvento'),
    path('procesarEdicionEvento/<int:titulo>/', views.procesar_edicion_evento, name='procesarEdicionEvento'),

    path('editar-registro/<int:id>/', views.editarRegistro, name='procesarEdicionRegistro'),
]
