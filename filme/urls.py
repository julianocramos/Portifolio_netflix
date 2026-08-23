from django.urls import path
from django.contrib.auth import views as auth_view

from .views import (
    DevFlixLoginView,
    Homefilmes,
    Detalhesfilme,
    Pesquisafilme,
    Paginaperfil,
    Criarconta,
    DemoSafePasswordChangeView,
)

app_name = 'filme'

urlpatterns = [
    path(
        '',
        DevFlixLoginView.as_view(),
        name='homepage'
    ),

    path(
        'filmes',
        Homefilmes.as_view(),
        name='homefilmes'
    ),

    path(
        'filmes/<int:pk>',
        Detalhesfilme.as_view(),
        name='detalhesfilme'
    ),

    path(
        'pesquisa/',
        Pesquisafilme.as_view(),
        name='pesquisafilme'
    ),

    path(
        'login/',
        DevFlixLoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        auth_view.LogoutView.as_view(
            template_name='logout.html'
        ),
        name='logout'
    ),

    path(
        'editarperfil/<int:pk>',
        Paginaperfil.as_view(),
        name='editarperfil'
    ),

    path(
        'criarconta/',
        Criarconta.as_view(),
        name='criarconta'
    ),

    path(
        'mudarsenha/',
        DemoSafePasswordChangeView.as_view(),
        name='mudarsenha'
    ),
]