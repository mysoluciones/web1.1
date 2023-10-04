from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from .forms import ContactoForm
from .models import Busqueda  # Importa el modelo Busqueda aquí

def busqueda(req, nombre, codigo):
    nueva_busqueda = Busqueda(nombre=nombre, codigo=codigo)
    nueva_busqueda.save()
    return HttpResponse(f"<p>Busqueda: {nueva_busqueda.nombre} - Codigo: {nueva_busqueda.codigo} CREADO CON EXITO</p>")

def inicio(req):
    return render(req, "inicio.html")

def quienessomos(req):
    return render(req, "quienessomos.html")

def quehacemos(req):
    return render(req, "quehacemos.html")

def portafolio(req):
    return render(req, "portafolio.html")

def contacto_exitoso(req):
    return render(req, "contacto_exitoso.html")

# Parte del formulario
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            nombre_apellido = form.cleaned_data['nombre_apellido']
            email = form.cleaned_data['email']
            asunto = 'REGISTRO DE CONSULTA EN MSW CREADO CON EXITO'
            mensaje = 'Su solicitud de contacto ha sido enviada a nuestros ejecutivos. Le adjuntamos un teléfono de contacto si desea ampliar su solicitud: +598 098075525 URUGUAY - + 54 9 3516076886 ARGENTINA'
            send_mail(asunto, mensaje, 'tucorreo@gmail.com', [email], fail_silently=False)
            send_mail('Nueva consulta de contacto', f'Nueva consulta de contacto de {nombre_apellido}', 'tucorreo@gmail.com', ['mysolucionessa@gmail.com'], fail_silently=False)
            return redirect('contacto_exitoso')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
