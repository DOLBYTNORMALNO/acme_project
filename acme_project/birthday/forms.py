from django import forms
from .validators import real_age
from .models import Birthday  # Импортируем модель


class BirthdayForm(forms.ModelForm):  # Используем ModelForm вместо Form
    class Meta:
        model = Birthday  # Указываем модель
        fields = '__all__'  # Используем все поля модели в форме
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
        # В аргументе validators указываем список или кортеж
        # валидаторов этого поля (валидаторов может быть несколько).
        validators = {
            'birthday': (real_age,),
        }