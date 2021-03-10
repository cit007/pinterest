from django.urls import path

from commentapp.views import CommentCreateView

from commentapp.views import CommentDeleteView

app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]
