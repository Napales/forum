from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from webapp.forms import TopicForm
from webapp.forms.search import SearchForm
from webapp.models import Topic

class TopicsListView(ListView):
    template_name = 'topics/topic_list.html'
    model = Topic
    context_object_name = 'topics'
    paginate_by = 5
    ordering = ['-created_at']

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs ):
        result = super().get_context_data(**kwargs)
        result['search_form'] = self.form
        if self.search_value:
            result['query'] = urlencode({'search': self.search_value})
            result['search'] = self.search_value
        return result

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


class TopicCreateView(CreateView):
    template_name = 'topics/topic_create.html'
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy('webapp:topic_list')
    # permission_required = 'webapp.add_project'

    # def has_permission(self):
    #     return super().has_permission()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicDetailView(DetailView):
    template_name = 'topics/topic_detail.html'
    model = Topic
    context_object_name = 'topic'
    # permission_required = 'webapp.view_project'
    #
    # def has_permission(self):
    #     return super().has_permission() and self.get_object().user.filter(pk=self.request.user.pk).exists()
