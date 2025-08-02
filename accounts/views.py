from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.forms.user_creation import MyUserCreationForm
from webapp.models import Topic

User = get_user_model()

class RegisterView(CreateView):
    template_name = 'user_create.html'
    model = User
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:topic_list')

class ProfileView(DetailView):
    template_name = 'profile_detail.html'
    model = User
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['topics'] = Topic.objects.filter(author=user).order_by('-created_at')
        return context
