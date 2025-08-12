from django import forms
from .models import Mother, Child, AnketaResponse

class MotherForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = [
            'first_name', 'last_name', 'fathers_name',
            'age_category', 'bmi_category', 'education', 'income_level',
            'has_chronic_illness', 'harmful_habits',
            'knowledge_level', 'mood_last_2_weeks',
            'passport_number', 'address',
        ]


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['birth_date', 'birth_weight']
        widgets = {
            'birth_date': forms.DateInput(attrs={
                'placeholder': 'yil-oy-kun',
                'type': 'date'  # adds browser calendar if supported
            })
        }



class AnketaResponseForm(forms.ModelForm):
    class Meta:
        model = AnketaResponse
        exclude = ['mother', 'child', 'score', 'risk_category']
