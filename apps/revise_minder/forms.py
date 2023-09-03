from django import forms
from apps.revise_minder.models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = []
        labels = {
            'description': 'Assunto',
            'color': 'Cor',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class':'subject-form-input',
                                                  'placeholder':'Escreva uma breve descrição'}),
            'color': forms.Select(attrs={'class':'subject-form-input'}),
        }