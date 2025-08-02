from django.urls import path

from webapp.views.topics import TopicsListView, TopicCreateView, TopicDetailView, TopicUpdateView, TopicDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', TopicsListView.as_view(), name='topic_list'),
    path('topic/add/', TopicCreateView.as_view(), name='topic_add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
]