from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import SignUpForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('home:index')

    def form_valid(self, form):
        messages.success(self.request, "ورود شما با موفقیت انجام شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "نام کاربری یا رمز عبور اشتباه است.")
        return super().form_invalid(form)

class CustomSignUpView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home:index')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomSignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todo:task_list")
        return super(CustomSignUpView, self).get(*args, **kwargs)
    