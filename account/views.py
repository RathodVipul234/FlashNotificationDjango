"""
    account views
"""
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User

from account.forms import RegistrationForm, LoginForm


class RegistrationView(CreateView):
    """
        Registration view class
    """
    template_name = 'register.html'
    success_url = '/'
    form_class = RegistrationForm

    def form_valid(self, form):
        """
            form valid method
        """
        super().form_valid(form)
        user, created = User.objects.get_or_create(
            username=self.object.username,
            first_name=self.object.first_name,
            last_name=self.object.last_name,
            email=self.object.email
        )
        user.set_password(self.request.POST.get('password'))
        user.is_active = True
        user.save()
        self.object.user = user
        self.object.save()
        messages.success(self.request, "User register successfully.")
        return redirect('login')


class LoginView(FormView):
    """
        Logout view
    """
    template_name = "login.html"
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        """
            custom dispatch mehtod
        """
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
    def get_form_kwargs(self):
        """
            get kwargs
        """
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """
            form valid method
        """
        messages.success(self.request, "User logged in successfully.")
        return redirect('/')


class LogoutView(FormView):
    """
        logout view
    """
    def get(self, *args, **kwargs):
        """
            get method for logout view
        """
        logout(self.request)
        messages.success(self.request, "User logged out successfully.")
        return redirect('/')
