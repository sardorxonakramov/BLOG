from django.urls import path

from .views import PostLView

urlpatterns=[
    path('', PostLView.as_view(), name='home'),
]