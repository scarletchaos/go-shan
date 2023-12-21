from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = "articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appname"] = "article"
        return context


# Create your views here.
