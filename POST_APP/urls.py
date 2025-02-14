from django.urls import path

from .views import PostLView, DetailPView, CreatePView, UpdatePView, DeletePView

urlpatterns = [
    path("", PostLView.as_view(), name="home"),
    path("post/<int:post_id>/", DetailPView.as_view(), name="detail"),
    path("create/", CreatePView.as_view(), name="create"),
    path("update/<int:post_id>/", UpdatePView.as_view(), name="update"),
    path("delete/<int:post_id>/", DeletePView.as_view(), name="delete"),
]
