from django.conf.urls import include, url
from weddingapp.views import *
from rest_framework.routers import DefaultRouter

# Register viewsets
router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    url(r"api/", include(router.urls)),
    url(r"^$", Home.as_view(), name="home"),
    url(r"^report", WeddingListReport.as_view(), name="report"),
]
