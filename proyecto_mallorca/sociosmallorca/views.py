from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Socio
import json

# Create your views here.

@csrf_exempt
def introducir_socio(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            dni = body.get('dni')
            numerosocio = body.get('numerosocio')
            contraseña = body.get('contraseña')

            Socio.objects.create(dni=dni, numerosocio=numerosocio, contraseña=contraseña)
            return JsonResponse({'mensaje': 'Socio creado correctamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def obtener_socio(request):
    if request.method == 'GET':
        socios = Socio.objects.all()
        lista_socios = [{'dni': Socio.dni, 'numerosocio': Socio.numerosocio} for Socio in socios]
        return JsonResponse({'Socios': lista_socios})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def borrar_socio(request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            dni = body.get('dni')
            socios = Socio.objects.get(dni=dni)
            socios.delete()
            return JsonResponse({'mensaje': 'Socio eliminado correctamente'})
        except Socio.DoesNotExist:
            return JsonResponse({'error': 'Socio no encontrado'}, status=404)
        
@csrf_exempt
def editar_contraseñasocio(request):
    
    string_body  = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    dni_socio = body['dni_socio']
    socio_contraseña= body['socio_contraseña']

    Socio.objects.filter(dni=dni_socio).update(contraseña = socio_contraseña)

    
    return JsonResponse({'mensaje': 'Clave actualizada correctamente'})

    


    
    