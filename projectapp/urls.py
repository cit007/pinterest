from django.urls import path
from django.views.generic import TemplateView

from projectapp.views import ProjectCreateView, ProjectDetailView

app_name = "projectapp"

urlpatterns = [
    # path('list/', TemplateView.as_view(template_name='projectapp/list.html'), name='list'),
    # path('list/', ProjectListView.as_view(), name='list'),

    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', ProjectUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', ProjectDeleteView.as_view(), name='delete'),
]
