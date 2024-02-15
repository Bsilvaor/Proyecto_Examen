from django.urls import path
from . import views

urlpatterns = [
    path('introducir_socio/', views.introducir_socio, name='introducir_socio'),
    path('obtener_socio/', views.obtener_socio, name='obtener_socio'),
    path('borrar_socio/', views.borrar_socio, name='borrar_socio'),
    path('editar_contraseñasocio/', views.editar_contraseñasocio, name='editar_contraseñasocio'),
]