from django.shortcuts import render, redirect, get_object_or_404
from .models import Frutas,  Galletitas ,Opinion
from django.http import JsonResponse
import json
from django.urls import reverse
from django.http import HttpResponse


def saludito(request):
    nombre_usuario = None
    edad_usuario = None
    if request.method == 'POST':
        nombre_ingresado = request.POST.get('nombre', '')
        edad_ingresada = int(request.POST.get('edad', 0))

        if edad_ingresada >= 18:
            if nombre_ingresado:
                nombre_usuario = nombre_ingresado
                edad_usuario = edad_ingresada
                return redirect('realizar_compra')
            else:
                mensaje = "Por favor, ingresa tu nombre."
                return render(request, 'mensaje_advertencia.html', {'mensaje': mensaje})
        else:
            mensaje = "Lo siento, debes tener al menos 18 años para acceder a esta página."
            return render(request, 'mensaje_advertencia.html', {'mensaje': mensaje})

    return render(request, 'saludar.html',  {'nombre_usuario': nombre_usuario, 'edad_usuario': edad_usuario})
    
def ver_comentarios(request):
    comentarios = Opinion.objects.all()  # Obtener todos los comentarios de la base de datos
    return render(request, 'ver_comentarios.html', {'comentarios': comentarios})

def mostrar_historia(request):
    
    return render(request, 'historia.html')

def detalles_galletas(request):
    galletas = Galletitas.objects.all()
    return render(request, 'galletas.html', {'galletas': galletas})


def opinion_form(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        opinion = request.POST.get('opinion')
        
        # Validar si el nombre o la opinión están vacíos
        if not nombre or not opinion:
            return HttpResponse("Por favor, asegúrate de completar ambos campos.")
        else:
            Opinion.objects.create(nombre=nombre, opinion=opinion)
            return render(request, 'gracias.html')
    return render(request, 'opinion_form.html')

def realizar_compra(request):
    frutas = Frutas.objects.all()
    if request.method == 'POST':
        compras = []

        for fruta in frutas:
            cantidad_key = f'cantidad_{fruta.id}'
            cantidad_str = request.POST.get(cantidad_key, '')

            if cantidad_str and cantidad_str.isdigit():
                cantidad = int(cantidad_str)
                if cantidad > 0:
                    precio = fruta.precio
                    compras.append({'fruta': fruta.nombre, 'cantidad': cantidad, 'precio': precio})

        total_cost = sum(compra['cantidad'] * compra['precio'] for compra in compras)

        # Convertir compras a JSON
        compras_json = json.dumps(compras)

        # Redirigir con la información de todas las compras y el total de todas las compras
        return redirect(reverse('recibo') + f'?total_cost={total_cost}&compras={compras_json}')

    return render(request, 'realizar_compra.html', {'frutas': frutas})


def lista_y_detalle_galletitas(request):
    if request.method == 'POST':
        galletita_seleccionada_id = request.POST.get('galletita_seleccionada')
        if galletita_seleccionada_id:
            galletita_seleccionada = Galletitas.objects.get(pk=galletita_seleccionada_id)
            request.session.setdefault('compras', []).append({
                'tipo': 'galletita',
                'nombre': galletita_seleccionada.nombre,
                
            })
            return redirect('lista_galletitas')
    galletitas_disponibles = Galletitas.objects.all()
    return render(request, 'lista_galletitas.html', {'galletitas': galletitas_disponibles})



def recibo(request):
    total_cost = float(request.GET.get('total_cost', 0))
    compras = request.GET.getlist('compras')

    # Ensure compras is a list of dictionaries
    compras = json.loads(compras[0]) if compras else []

    # Calculate total price for each item
    for compra in compras:
        compra['total_price'] = compra['precio'] * compra['cantidad']

    return render(request, 'recibo.html', {'compras': compras, 'total_cost': total_cost})