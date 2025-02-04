from django import forms
from django.contrib.auth.forms import AuthenticationForm
from portfolio.models import ValetCars, get_model_by_name

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class AllCarsForm(forms.ModelForm):
    class Meta:
        model = ValetCars
        exclude = ['guestID']

def get_dynamic_form(model_name):
    model_info = get_model_by_name(model_name)
    if not model_info:
        raise ValueError(f"Model '{model_name}' not found.")

    model, required_fields = model_info

    return type(
        "DynamicValetForm",
        (forms.ModelForm,),
        {
            "Meta": type("Meta", (), {"model": model, "fields":[field for field in required_fields if field != 'guestID']}),
            "__init__": lambda self, *args, **kwargs: super(self.__class__, self).__init__(*args, **kwargs)
        }
    )