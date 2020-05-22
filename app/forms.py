from django import forms
from .models import Producto, Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'sku', 'nombre',
                  'descripcion', 'clasificacion', 'precio', ]
        labels = {'codigo': 'Codigo EAN', 'sku': 'Codigo Interno', 'nombre': 'Nombre', 'descripcion': 'Descripcion Producto',
                  'clasificacion': 'Clasificación', 'precio': 'Precio Producto', 'disponible': 'Stock Disponible'}
        widgets = {'codigo': forms.TextInput(attrs={'class': 'form-control'}),
                   'sku': forms.TextInput(attrs={'class': 'form-control'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                   'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
                   'precio': forms.TextInput(attrs={'class': 'form-control'}),
                   'disponible': forms.TextInput(attrs={'class': 'form-control'}), }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['producto', 'rut', 'nombre_empresa',
                  'telefono', 'domicilio', 'region', 'comuna']
        labels = {'producto': 'Producto', 'rut': 'Rut', 'nombre_empresa': 'Nombre Empresa', 'telefono': 'Teléfono', 'domicilio': 'Domicilio',
                  'region': 'Región', 'comuna': 'Comuna'}



