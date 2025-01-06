from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Evento, Registro
from django.contrib import messages



# Página principal que lista eventos y registros
def home(request):
    eventoBdd = Evento.objects.all()
    registroBdd = Registro.objects.all()
    return render(request, "listadoEventos.html", {'Eventos': eventoBdd, 'Registros': registroBdd})

# Guardar un nuevo evento
def guardarEvento(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        fecha = request.POST.get("fecha", "")
        hora = request.POST.get("hora", "")
        ubicacion = request.POST.get("ubicacion", "").strip()
        estado = request.POST.get('estado') == 'True' 
        
        # Validar campos obligatorios
        if not titulo or not fecha or not hora:
            messages.error(request, "Título, fecha y hora son obligatorios.")
            return redirect('/')
        
        # Crear el evento
        Evento.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            categoria=categoria,
            fecha=fecha,
            hora=hora,
            ubicacion=ubicacion,
            estado=estado
        )
        messages.success(request, "Evento guardado exitosamente")
        return redirect('/')
    else:
        messages.error(request, "Método de solicitud no válido.")
        return redirect('/')

# Guardar un nuevo registro asociado a un evento
def guardarRegistro(request):
    if request.method == "POST":
        evento_id = request.POST.get("evento", "")
        nombre_participante = request.POST.get("nombre_participante", "").strip()
        email = request.POST.get("email", "").strip()
        
        # Validar campos obligatorios
        if not nombre_participante or not email or not evento_id:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('/')
        
        try:
            evento = Evento.objects.get(id=evento_id)
            Registro.objects.create(
                evento=evento,
                nombre_participante=nombre_participante,
                email=email
            )
            messages.success(request, "Registro guardado exitosamente.")
        except Evento.DoesNotExist:
            messages.error(request, "El evento seleccionado no existe.")
        return redirect('/')
    else:
        messages.error(request, "Método de solicitud no válido.")
        return redirect('/')

# Eliminar un evento por su título
def eliminarEvento(request, titulo):
    try:
        evento = Evento.objects.get(titulo=titulo)
        evento.delete()
        messages.success(request, "Evento eliminado exitosamente.")
    except Evento.DoesNotExist:
        messages.error(request, "El evento no existe.")
    return redirect('/')

# Eliminar un registro por su ID
def eliminarRegistro(request, registro_id):
    try:
        registro = Registro.objects.get(id=registro_id)
        registro.delete()
        messages.success(request, "Registro eliminado exitosamente.")
    except Registro.DoesNotExist:
        messages.error(request, "El registro no existe.")
    return redirect('/')

def editarEvento(request, titulo):
   
    evento = get_object_or_404(Evento, titulo=titulo)
    
    if request.method == 'POST':
        
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        
        evento.save()
        return redirect('evento_lista')  

    return render(request, 'editarEvento.html', {'evento': evento})


def editarRegistro(request, id):
    registro = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listadoRegistro') 
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'editarRegistro.html', {'form': form})


def procesar_edicion_evento(request, id_evento): 
    evento = get_object_or_404(Evento, id=titulo) 
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        evento.categoria = request.POST.get('categoria')
        evento.fecha = request.POST.get('fecha')
        evento.hora = request.POST.get('hora')
        evento.ubicacion = request.POST.get('ubicacion')
        evento.estado = request.POST.get('estado')
        evento.save()
        return redirect('home')