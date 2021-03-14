from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article

from likeapp.models import Like


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        like = Like.objects.filter(user=user, article=article)
        if like.exists():
            like.delete()
            article.good -= 1
            article.save()
            messages.add_message(
                self.request, messages.ERROR, "LIKEを取消しました。")
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            Like(user=user, article=article).save()
            article.good += 1
            article.save()
            messages.add_message(
                self.request, messages.INFO, "LIKEをありがとう御座います。")

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
