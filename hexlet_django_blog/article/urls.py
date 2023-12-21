from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.IndexPageView.as_view(template_name="articles.html"), name="articles_index"),
]
