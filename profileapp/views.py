from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm

from profileapp.decorators import profile_custom_ownership_required


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)

    # HOW TO ACCESS [accountapp/detail/pk] - success_url = reverse_lazy('accountapp:detail')
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_custom_ownership_required, 'get')
@method_decorator(profile_custom_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    # HOW TO ACCESS [accountapp/detail/pk] - success_url = reverse_lazy('accountapp:detail')
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
