from django import forms
from django.contrib.auth.forms import AuthenticationForm
from portfolio.models import ValetCars, get_model_by_name

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class AllCarsForm(forms.ModelForm):
    class Meta:
        model = ValetCars
        fields = '__all__'

def get_dynamic_form(model_name):
    model_info = get_model_by_name(model_name)
    if not model_info:
        raise ValueError(f"Model '{model_name}' not found.")
    
    model, required_fields = model_info

    class DynamicValetForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(DynamicValetForm, self).__init__(*args, **kwargs)
            for field_name in required_fields:
                if field_name in self.fields:
                    self.fields[field_name].required = True
            for field_name, field in self.fields.items():
                if field_name not in required_fields:
                    field.required = False

        class Meta:
            model_class = get_model_by_name(model_name)
            model = model_class[0]
            fields = '__all__'

    return DynamicValetForm