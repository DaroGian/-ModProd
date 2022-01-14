from django import forms

class cursoform(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    