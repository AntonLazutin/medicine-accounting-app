from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout

class HomePage(View):
    
    def get(self, *args, **kwargs):
        return render(self.request, 'home/index.html')


class LoginPageView(LoginView):
    template_name = 'home/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class LogoutPageView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect((reverse_lazy('home')))