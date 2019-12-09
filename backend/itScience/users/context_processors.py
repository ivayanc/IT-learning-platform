from .forms import SystemUserCreationForm, SystemUserLoginForm

def add_login_forms(request):
    return {
        'registration_form': SystemUserCreationForm(),
        'login_form': SystemUserLoginForm(),
    }