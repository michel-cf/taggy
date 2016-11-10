from django.conf.urls import url, include
from rest_framework import routers

from members import rest as members_rest

router = routers.DefaultRouter()
router.register(r'member', members_rest.MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
