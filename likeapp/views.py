from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article

from likeapp.models import Like


@transaction.atomic
def db_transaction(self, user, article):
    like = Like.objects.filter(user=user, article=article)
    if like.exists():
        like.delete()
        article.good -= 1
        article.save()

        # return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': article.pk}))
        return False
    else:
        Like(user=user, article=article).save()
        article.good += 1
        article.save()

        return True


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        try:
            result = db_transaction(self, user, article)
            if(result == True):
                messages.add_message(
                    self.request, messages.INFO, "「LIKE」ありがとう御座います。")
            else:
                messages.add_message(
                    self.request, messages.ERROR, "「LIKE」取消しました。")
        except:
            messages.add_message(
                self.request, messages.ERROR, "「LIKE」更新できませんでした。")

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
