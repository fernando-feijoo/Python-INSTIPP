from django import forms

from .models import Categoria, SubCategoria, Marca


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': "Sub Categoría",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Provincia"


class MarcaForm(forms.ModelForm):
    
    cedula = forms.CharField(label="Cédula")
    apellido = forms.CharField(label="Apellido")
    nombre = forms.CharField(label="Nombre")
    direccion = forms.CharField(label="Dirección")
    ciudad = forms.CharField(label="Ciudad")
    telefono = forms.CharField(label="Teléfono")

    class Meta:
        model = Marca
        fields = ['cedula', 'apellido', 'nombre',
                  'direccion', 'ciudad', 'telefono', 'estado']
        labels = {
            'cedula': "Cédula",
            'apellido': "Apellido",
            'nombre': "Nombre",
            'direccion': "Dirección",
            'ciudad': "Ciudad",
            'telefono': "Teléfono",
            'estado': "Estado",
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
