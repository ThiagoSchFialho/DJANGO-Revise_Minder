from django import forms
from apps.revise_minder.models import Subject, Study

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['user',]
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
        fields = ['subject', 'revisions_cycles', 'date']
        exclude = ['is_done', 'user',]
        labels = {
            'subject': 'Assunto',
            'revisions_cycles': 'Número de Revisões',
            'date': 'Data do Estudo'
        }
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-list-input'}),
            'revisions_cycles': forms.NumberInput(attrs={
                'class': 'form-list-input',
                'min': '1',
                'max': '3',
            }),
            'date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-list-input'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(StudyForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['subject'].queryset = Subject.objects.filter(user=user)
