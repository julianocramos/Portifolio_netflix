from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView

from .models import Filme, Usuario
from .forms import CriarContaForm


DEMO_USERNAME = 'demo@devflix.app'
DEMO_PASSWORD = 'DevFlixDemo2026!'


def ensure_demo_user():
    """
    Ensures that the public portfolio demo account exists.

    The account has no staff or administrator privileges.
    If someone changes the public demo password, it is restored
    the next time the login page is accessed.
    """

    user, created = Usuario.objects.get_or_create(
        username=DEMO_USERNAME,
        defaults={
            'email': DEMO_USERNAME,
            'first_name': 'Demo',
            'last_name': 'User',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
        }
    )

    changed = False

    if user.email != DEMO_USERNAME:
        user.email = DEMO_USERNAME
        changed = True

    if user.first_name != 'Demo':
        user.first_name = 'Demo'
        changed = True

    if user.last_name != 'User':
        user.last_name = 'User'
        changed = True

    if not user.is_active:
        user.is_active = True
        changed = True

    if user.is_staff:
        user.is_staff = False
        changed = True

    if user.is_superuser:
        user.is_superuser = False
        changed = True

    if not user.check_password(DEMO_PASSWORD):
        user.set_password(DEMO_PASSWORD)
        changed = True

    if changed:
        user.save()

    return user


class DevFlixLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        ensure_demo_user()
        return super().dispatch(request, *args, **kwargs)


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()

        filme.visualizacoes += 1
        filme.save()

        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filmes_relacionados = Filme.objects.filter(
            categoria=self.get_object().categoria
        )[:3]

        context['filmes_relacionados'] = filmes_relacionados

        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')

        if termo_pesquisa:
            return self.model.objects.filter(
                titulo__icontains=termo_pesquisa
            )

        return self.model.objects.none()


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def dispatch(self, request, *args, **kwargs):
        if request.user.username == DEMO_USERNAME:
            return redirect('filme:homefilmes')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('filme:homefilmes')


class DemoSafePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'editarperfil.html'
    success_url = reverse_lazy('filme:homefilmes')

    def dispatch(self, request, *args, **kwargs):
        if request.user.username == DEMO_USERNAME:
            return redirect('filme:homefilmes')

        return super().dispatch(request, *args, **kwargs)


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')