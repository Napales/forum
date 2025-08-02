from django.urls import path

from webapp.views.topics import TopicsListView

app_name = 'webapp'
urlpatterns = [
    path('', TopicsListView.as_view(), name='topics_list'),
]