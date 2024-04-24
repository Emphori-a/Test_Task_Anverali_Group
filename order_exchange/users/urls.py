from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm
from .views import UserProfileDetailView, UserProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=RegistrationForm,
            success_url=reverse_lazy('users:login'),
        ),
        name='registration',
    ),
    path('profile/<str:username>/', UserProfileDetailView.as_view(),
         name='user_profile'),
    path('profile/', UserProfileUpdateView.as_view(),
         name='edit_profile'),
]
