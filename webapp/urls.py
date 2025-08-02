from django.urls import path

from webapp.views.comments import CommentUpdateView, CommentCreateView
from webapp.views.topics import TopicsListView, TopicCreateView, TopicDetailView, TopicUpdateView, TopicDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', TopicsListView.as_view(), name='topic_list'),
    path('topic/add/', TopicCreateView.as_view(), name='topic_add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),



    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('topic/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_create'),

]