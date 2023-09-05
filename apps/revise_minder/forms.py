from django import forms
from apps.revise_minder.models import Subject, Study

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = []
        labels = {
            'description': 'Assunto',
            'color': 'Cor',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class':'form-list-input',
                                                  'placeholder':'Escreva uma breve descrição'}),
            'color': forms.Select(attrs={'class':'form-list-input'}),
        }

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        exclude = ['is_done']
        labels = {
            'subject': 'Assunto',
            'revisions_cycles': 'Número de Revisões',
            'date': 'Data do Estudo',
            'user': 'Usuário'
        }
        widgets = {
            'subject': forms.Select(attrs={'class':'form-list-input'}),
            'revisions_cycles': forms.NumberInput(attrs={
                'class':'form-list-input',
                'min':'1',
                'max':'3',
                }),
            'date': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-list-input'
                }
            ),
            'user': forms.Select(attrs={'class':'form-list-input'})
        }