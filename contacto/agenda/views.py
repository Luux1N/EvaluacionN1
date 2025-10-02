


from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

def lista_contactos(request):
    query = request.GET.get('q') 
    if query:
        contactos = Contacto.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query)) # filtra por nombre o correo
    else:
        contactos = Contacto.objects.all() # trae todos
    return render(request, 'agenda/lista_contactos.html', {'contactos': contactos, 'q': query})

def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST) # recibe datos
        if form.is_valid():
            form.save() # guarda contacto
            return redirect('lista_contactos')
    else:
        form = ContactoForm() # formulario vacio
    return render(request, 'agenda/agregar_contacto.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk) # trae contacto
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save() # guarda cambios
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto) # formulario con datos
    return render(request, 'agenda/editar_contacto.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk) # trae contacto
    if request.method == 'POST':
        contacto.delete() # elimina contacto
        return redirect('lista_contactos')
    return render(request, 'agenda/eliminar_contacto.html', {'contacto': contacto})