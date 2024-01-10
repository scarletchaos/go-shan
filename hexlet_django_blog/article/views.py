from django.shortcuts import render
from django.views import View



class IndexView(View):
    template_name = "articles.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"appname": "article"})



# Create your views here.
