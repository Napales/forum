from webapp.forms.base_form import BaseForm
from webapp.models import Topic


class TopicForm(BaseForm):

    class Meta:
        model = Topic
        fields = ('name', 'description')