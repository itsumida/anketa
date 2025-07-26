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
        ]


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['birth_date', 'birth_weight']


class AnketaResponseForm(forms.ModelForm):
    class Meta:
        model = AnketaResponse
        exclude = ['mother', 'child', 'score', 'risk_category']
