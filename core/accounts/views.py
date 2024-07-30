from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        print(f"Next URL: {next_url}")  # برای عیب‌یابی
        if next_url:
            return next_url
        return reverse_lazy('home:index')

    def form_valid(self, form):
        messages.success(self.request, "ورود شما با موفقیت انجام شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "نام کاربری یا رمز عبور اشتباه است.")
        return super().form_invalid(form)
