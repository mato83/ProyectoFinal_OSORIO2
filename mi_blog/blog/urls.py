from django.urls import path, include
from .views import (
    PageListView, PageDetailView, InicioView, PageCreateView,
    PageDeleteView, PageUpdateView, ContactoView, AcercaDeView,
    ProfileUpdateView, ProfileView, SignUpView
)
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('paginas/', PageListView.as_view(), name='page-list'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('page/nuevo/', PageCreateView.as_view(), name='page-create'),
    path('page/<int:pk>/editar/', PageUpdateView.as_view(), name='page-update'),
    path('page/<int:pk>/borrar/', PageDeleteView.as_view(), name='page-delete'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('acerca/', AcercaDeView.as_view(), name='acerca'),
    path('perfil/', ProfileView.as_view(), name='profile'),
    path('perfil/editar/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
