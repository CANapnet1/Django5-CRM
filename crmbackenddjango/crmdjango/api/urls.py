from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientDetailsViewSet, JoinedTablesView


router = DefaultRouter()
router.register(r"client", ClientViewSet)
router.register(r"client-details", ClientDetailsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("joinedtables/", JoinedTablesView.as_view(), name="joined-tables"),
]