from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from projectapp.models import Project

from projectapp.forms import ProjectCreationForm


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    context_object_name = 'target_project'
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})
