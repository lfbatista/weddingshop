from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from weddingapp.serializers import *


# App views
class Home(View):
    template = "home.html"
    context = {
        "page_title": "Home",
    }

    def get(self, request):
        return render(request, self.template, self.context)


class WeddingListReport(View):
    template = "report.html"
    context = {
        "page_title": "Report",
    }

    def get(self, request):
        return render(request, self.template, self.context)


# API resources
class ProductViewSet(viewsets.ModelViewSet):
    """
    List all products or get, create, update or delete a product.
    Search parameters are "brand" and "name".
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ("brand", "name", )

