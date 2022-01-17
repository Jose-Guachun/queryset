from django.shortcuts import render, redirect
from crud.models import Marca, Modelo, Producto
from crud.forms import ProductoForm

def list(request):
    productos=Producto.objects.all()
    return render(request,'productos/index.html',{'productos':productos})

def create(request):
    if request.method=='POST':
        form=ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            product = Producto()
            product.marca = form.cleaned_data['marca']
            product.modelo = form.cleaned_data['modelo']
            product.descripcion = form.cleaned_data['descripcion']
            product.fecha = form.cleaned_data['fecha']
            product.cantidad = form.cleaned_data['cantidad']
            product.precio = form.cleaned_data['precio']
            product.total =  product.cantidad*product.precio
            product.save()
            return redirect('crud:index')
    else:
        form=ProductoForm()

    return render(request,'productos/create.html',{'form':form})

def update(request,id):
    producto=Producto.objects.get(id=id)
    if request.method=='GET':
        form=ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            product = Producto()
            product.marca = form.cleaned_data['marca']
            product.modelo = form.cleaned_data['modelo']
            product.descripcion = form.cleaned_data['descripcion']
            product.fecha = form.cleaned_data['fecha']
            product.cantidad = form.cleaned_data['cantidad']
            product.precio = form.cleaned_data['precio']
            product.total = product.cantidad * product.precio
            product.save()
            return redirect('crud:index')

    return render(request,'productos/create.html',{'form':form})

def delete(request,id):
    producto = Producto.objects.get(id=id)
    descripcion=producto.descripcion
    if request.method=='POST':
        producto.delete()
        return redirect('crud:index')
    return render(request,'productos/delete.html',{'descripcion':descripcion})

