from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm,
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]